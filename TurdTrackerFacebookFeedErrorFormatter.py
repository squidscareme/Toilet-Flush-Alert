class TurdTrackerFacebookFeedErrorFormatter:
	
	def __init__(self):
		pass

	'''Formats the error to a nice informative string'''
	def formatErrorCode(self, response):
		return response.reason + " --- " + response.text
