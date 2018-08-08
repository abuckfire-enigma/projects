import argparse
import collections
import itertools
import operator
import sqlite3
import tabulate
import unicodecsv as csv

DATABASES_OF_INTEREST = {"urls": ["last_visit_time", "epoch_last_visit", "url", "title", "visit_count"],
                         "visits": ["id", "url", "visit_time", "from_visit", "transition", "segment_id", "visit_duration"],
                         "keyword_search_terms": ["keyword_id", "url_id", "lower_term", "term"],
                         "downloads": ["start_time", "current_path", "received_bytes", "total_bytes", "danger_type", "interrupt_reason", "opened", "last_access_time", "site_url", "tab_url", "mime_type", "last_modified"]}

def parse(row, headers):
    return dict(itertools.izip(headers, row))

def get_database_contents(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    return cursor.execute('SELECT datetime(last_visit_time/1000000-11644473600, "unixepoch") as last_visited, last_visit_time, url , title, visit_count FROM urls;')

def write_chrome_history_to_csv(file_path, headers, db_rows):
    with open(file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for row in db_rows:
            writer.writerow(parse(row, headers))

def get_base_url(url):
    return url["url"].split("/")[2]

def column_to_count_dict(file_path, field):
    counter = collections.defaultdict(int)
    with open(file_path, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if field == "url":
                counter[get_base_url(row)] += 1
            else:
                counter[row[field]] += 1
    return sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

def create_table(data, headers):
    data_list = [[d[0], d[1]] for d in data]
    return tabulate.tabulate(data_list, headers=headers)

def compile_report(frequency_of_visits, page_titles, peak_useage_times):
    pass

def main():
    parser = argparse.ArgumentParser("Analyze chrome history")
    parser.add_argument("-p", "--pull_data", default=False, help="pull most recent data")
    parser.add_argument("-t", "--target", default="sites_visited.csv", help="directory to write the history to")
    parser.add_argument("-d", "--database", default="~/Library/Application\\ Support/Google/Chrome/Default/History", help="path to the database for your browser history")
    args = parser.parse_args()

    if args.pull_data: # pull and write data
        database_contents = get_database_contents(args.database)
        write_chrome_history_to_csv(args.target, DATABASES_OF_INTEREST["urls"], database_contents)

    print create_table(column_to_count_dict(args.target, "url"), ["url", "visits"])
    print create_table(column_to_count_dict(args.target, "title"), ["title", "visits"])


if __name__ == "__main__":
    main()
