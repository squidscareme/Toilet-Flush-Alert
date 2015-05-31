from TurdTrackerConfiguration import TurdTrackerConfiguration

class TurdTrackerFacebookFeedPayloadService:

	def __init__(self):
		self._config = TurdTrackerConfiguration()

	def _getMessage(self):
		return "someone flushed"

	'''returns an object to post to facebook'''
	def getPostFeedPayload(self):
		return {"access_token":self._config.getFacebookAccessToken(), "message": self._getMessage()}
