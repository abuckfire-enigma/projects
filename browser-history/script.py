import argparse
import collections
import itertools
import os
import sqlite3
import unicodecsv as csv

DATABASES_OF_INTEREST = {"urls": ["last_visit_time", "url" , "title", "visit_count", "hidden"],
                         "visits": ["id", "url", "visit_time", "from_visit", "transition", "segment_id", "visit_duration"],
                         "keyword_search_terms": ["keyword_id", "url_id", "lower_term", "term"],
                         "downloads": ["start_time", "current_path", "received_bytes", "total_bytes", "danger_type", "interrupt_reason", "opened", "last_access_time", "site_url", "tab_url", "mime_type", "last_modified"]}

def parse(row, headers):
    return dict(itertools.izip(headers, row))

def get_database_contents(database_path):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    return c.execute('SELECT datetime(last_visit_time/1000000-11644473600, "unixepoch") as last_visited, last_visit_time, url , title, visit_count, hidden FROM urls;')

def write_chrome_history_to_csv(file_path, headers, db_rows):
    with open(file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for row in db_rows:
            writer.writerow(parse(row, headers))

def get_base_url(url):
    return url["title"].split("/")[2]

def get_dictionary(file_path):
    url_counter = collections.defaultdict(int)
    with open(file_path, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            url_counter[get_base_url(row)] += 1
    print url_counter

def main():
    parser = argparse.ArgumentParser("Analyze chrome history")
    parser.add_argument("-p", "--pull_data", default=False, help="pull most recent data")
    parser.add_argument("-t", "--target", default="sites_visited.csv", help="directory to write the history to")
    parser.add_argument("-d", "--database", required=True, help="path to the database for your browser history")
    args = parser.parse_args()

    if args.pull_data: # pull and write data
        database_contents = get_database_contents(args.database)
        write_chrome_history_to_csv(args.target, DATABASES_OF_INTEREST["urls"], database_contents)
    
    get_dictionary(args.target)

if __name__ == "__main__":
    # python script.py -p True -d /Users/abuckfire/Library/Application\ Support/Google/Chrome/Default/History
    main()
