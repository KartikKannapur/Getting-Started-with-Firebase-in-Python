__author__ = "Kartik Kannapur"
__date__ = "22-08-2015"

# #Python Library Imports
from firebase import firebase

from multiprocessing import Process
from sseclient import SSEClient
import json
import time


# #File Imports
import properties as prop


class FirebaseApp(object):
	"""
	1. Using the Firebase API.
	2. Simple Chat Application with Firebase
	"""
	def __init__(self):
		print "\n\n\n--- My Firebase App ---"


	def firebase_data(self):
		# #Firebase Application URL
		fbase = firebase.FirebaseApplication(prop.prop_firebase_url, None)

		# #Read all the data as JSON
		result = fbase.get('', None)
		print result
		print "\n\n\n"

		
		# #Read the value 'community name'
		result_community_name = fbase.get('community_name', None)
		print result_community_name
		print "\n\n\n"


		# #Insert 'event_time'
		result_community_name = fbase.post('event_time', "4 to 6 PM")
		print result_community_name
		print "\n\n\n"


		# #Read all the data as JSON
		result = fbase.get('', None)
		print result
		print "\n\n\n"



	def firebase_chat_application(self):
		# #Server-Sent Events with  - Streaming
		ss_event = SSEClient(prop.prop_gdgbangalore_chat_url + "Messages.json")

		print("\n\nFirebase Server - %s" % (prop.prop_gdgbangalore_chat_url + "Messages.json"))


		for new_message in ss_event:
			message_data = json.loads(new_message.data)
			# print new_message

			if message_data is None:
				continue

			# #Read old messages when the user was not active on the chat
			if message_data["path"] == "/": 
				print("\nWhen you weren't there ... \n")
				for (nodeid, message) in message_data["data"].items():
					try:
						print("%s says: %s" % (message["name"], message["message"]))
						# print "\n"
					except:
						pass

			# #New Message
			else: 
				try:
					print("%s says: %s" % (message_data["data"]["name"], message_data["data"]["message"]))
					# print "\n"
				except:
					pass

	

if __name__ == '__main__':
	my_firebase = FirebaseApp()
	# my_firebase.firebase_data()


	# Start a thread to monitor changes to firebase
	chat_app = Process(target=my_firebase.firebase_chat_application)
	chat_app.start()

	time.sleep(1)
	username = raw_input("Username: ")
	fb = firebase.FirebaseApplication(prop.prop_gdgbangalore_chat_url, None)

	# Post initial message to Firebase
	fb.post('Messages',
			{"name": username,
			 "message": "Joined the chat",
			 ".priority": time.time() * 1000
			})

	# Post new messages to Firebase
	while (True):
		message = raw_input("")
		print("\n")
		fb.post('Messages',
				{
					"name": username,
					"message": message,
					".priority": time.time() * 1000
				})

