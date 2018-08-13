import bot_functions

#Get login credentials
login = bot_functions.bot_login()
#Subreddit the bot will look inside of
subreddit = "nba"
#Word the bot will look for
word = "lebron"
#Get saved comment IDs
comment_id = bot_functions.get_saved_comments()
#Number of comments to search
limit = "100"


