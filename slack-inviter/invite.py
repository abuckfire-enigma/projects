import argparse
import logging
import sys

from slacker import Slacker, Error


def get_arguments():
    """Parse CL arguments
    """
    parser = argparse.ArgumentParser("Bulk invite users to a slack channel")
    parser.add_argument("-k", "--api_key_file", required=False, default="api_key.txt", help="path to file that contains the api key")
    parser.add_argument("-c", "--channel_name", required=True, help="channel to invite users to be in")
    parser.add_argument("-u", "--users", required=False, type=list, help="list specific users to bulk invite")
    return parser.parse_args()


def configure_logging():
    """Configure logging
    """
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="[%(asctime)s] %(message)s"
    )


def make_slack_object(api_file):
    """Takes API key and returns Slack object for querying corresponding slack domain
    Args:
        api_file (str): path to the file containing the api key
    Returns:
        Slacker object
    """
    try:
        return Slacker(open(api_file).read().strip())
    except IOError, AssertionError:
        logging.warning("Cannot find file path or other reading error")


def get_channel_id(slack, channel_name):
    """Gets channel id for provided channel name
    Args:
        slack: object for querying the Slack api 
        channel_name (str)
    Returns:
        ID string of the channel name
    """
    response = slack.channels.list()
    channel = [d for d in response.body["channels"] if d["name"] == channel_name]
    if not channel:
        logging.warning("Cannot find channel {}".format(channel_name))
    return channel[0]["id"]


def get_users(slack, users=[]):
    """Gets user IDs for list of users. Defaults to all users
    Args:
        slack: object for querying the Slack api 
        users (list): user names to find the IDs for
    Returns:
        list of tuples of (user_id, user_name)
    """
    members = slack.users.list().body["members"]
    if users:
        return [(user["id"], user["name"]) for user in members if user["name"] in users]
    return [(user["id"], user["name"]) for user in members if user["is_bot"] == False]


def bulk_invite_users(slack, users, channel_id):
    """Invite users to a slack channel
    Args:
        slack: object for querying the Slack api 
        users: list of tuples of (user_id, user_name)
        channel_id: ID of the channel to invite users to
    """
    logging.info("Inviting Users:")
    for user_id, username in users:
        try:
            slack.channels.invite(channel_id, user_id)
            logging.info(username)
        except Error as e:
            code = e.args[0]
            if code == "already_in_channel":
                logging.info("{} is already in the channel".format(username))
            if code in ["cant_invite_self", "cant_invite", "user_is_ultra_restricted"]:
                logging.info("Skipping user {} for reason: {}".format(username, code))


def main():
    """Takes CL arguments:
    - an api key for a corresponding slack domain
    - channel name
    - (optional) list of usernames
    and proceeds to bulk invite the users to the specified channel
    """
    args = get_arguments()
    slack = make_slack_object(args.api_key_file)
    bulk_invite_users(slack, get_users(slack, args.users), get_channel_id(slack, args.channel_name))


if __name__ == "__main__":
    main()
