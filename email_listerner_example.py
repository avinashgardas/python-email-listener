import email_listener

user = '<EMAIL>'
password = '<PASSWORD>'
folder = 'Inbox'
# unread emails would be saved here
attachment_dir = "attachments"

con = email_listener.EmailListener(user, password, folder, attachment_dir)

con.login()

# read the currently unread email in the FOLDER
messages = con.scrape()
print(messages)

# listen to inbox with time out to be 30 seconds
con.listen(30)