# Tool for Inviting Users to a Slack Channel
Useful for inviting a larger subset of users

## To Use:
1. Put your API key for a Slack domain into a `txt` file
2. Invoke the inviter with `python invite.py -c <channel_name> -k <path_to_api_txt_file> -u [<list of users>]`
    * The default api file key path is set to `api_key.txt` (i.e. current directory)
    * If you do not specify a list of users, the program defaults to inviting everyone with a username for the Slack domain (excluding bots)
