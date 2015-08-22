__author__ = "Kartik Kannapur"
__date__ = "22-08-2015"

# #Python Library Imports
from firebase import firebase


# #File Imports
import properties as prop


class FirebaseApp(object):
	"""
	Simple Operations on Firebase
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








if __name__ == '__main__':
	my_firebase = FirebaseApp()
	my_firebase.firebase_data()
