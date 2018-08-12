import config
import praw
import time
import os

def bot_login():
		print "Logging in..."
		login = praw.Reddit(username = config.username,
	        			password = config.password,
	        			client_id = config.client_id,
	        			client_secret = config.client_secret,
	        			user_agent = "FinderBot v0.1")
		print "Logged in!"
    
    		return login

def run_bot(login, subreddit, word, comment_id, limit):
		print "Obtaining "+ limit + " comments..."

   		for comment in login.subreddit(subreddit).comments(limit = limit):
   	 		if word in comment.body and comment.id not in comment_id:
   	 			print "Comment with \""+ word +"\" has been found! Comment ID: " + comment.id
   	 			
   	 			comment_id.append(comment.id)
   	 			print "Comment ID has been added to the list."

   	 			with open ("comment_id.txt", "a") as f:
   	 					f.write(comment.id + "\n")

   	 			with open ("comments_recorded.txt", "a") as f:
   	 					author = " --" + str(comment.author)
   	 					time_posted = " --" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(comment.created))
   	 					body = comment.body.encode('utf-8')
   	 					f.write(body + author + time_posted + "\n\n\n")

   		print "Sleeping for 10 seconds..."
   		time.sleep(10)

def get_saved_comments():

		if not os.path.isfile("comment_id.txt"):
				comment_id = []
		else:
				with open("comment_id.txt", "r") as f:
						comment_id = f.read()
						comment_id = comment_id.split("\n")
						comment_id = filter(None, comment_id)

		return comment_id