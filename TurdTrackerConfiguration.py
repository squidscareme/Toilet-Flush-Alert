import os

class TurdTrackerConfiguration:
	def __init__(self):
		pass

	'''Gets the access token with permission to post to facebook feed'''
	def getFacebookAccessToken(self):
		return os.environ.get("TURDTRACKER_FACEBOOK_TOKEN") 

	'''Gets the Facebook page if to post to'''
	def getFacebookPageId(self):
		return os.environ.get("TURDTRACKER_FACEBOOK_PAGE_ID")

	'''Gets the Facebook API version, currently 2.3'''
	def getFacebookApiVersion(self):
		return os.environ.get("TURDTRACKER_FACEBOOK_API_VERSION")