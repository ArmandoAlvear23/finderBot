import bot_params
import bot_functions

login = bot_params.login
subreddit = bot_params.subreddit
word = bot_params.word
comment_id = bot_params.comment_id
limit = bot_params.limit

print comment_id
while True:
	bot_functions.run_bot(login, subreddit, word, comment_id, limit)