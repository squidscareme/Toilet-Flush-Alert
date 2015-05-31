import requests
from TurdTrackerFacebookFeedErrorFormatter import TurdTrackerFacebookFeedErrorFormatter
from TurdTrackerFacebookFeedPayloadService import TurdTrackerFacebookFeedPayloadService
from TurdTrackerConfiguration import TurdTrackerConfiguration

class TurdTrackerFacebookFeedPost:

	def __init__(self):
		self._errorFormatter = TurdTrackerFacebookFeedErrorFormatter()
		self._payloadService = TurdTrackerFacebookFeedPayloadService()
		self._configuration = TurdTrackerConfiguration()
		self._feedPostUrl = "https://graph.facebook.com/v" + self._configuration.getFacebookApiVersion() + "/" + self._configuration.getFacebookPageId() + "/feed"

	'''inform facebook that someone flushed the toilet'''
	def informFacebookOfToiletFlush(self):
		payload = self._payloadService.getPostFeedPayload()

		response = requests.post(self._feedPostUrl, data=payload)

		if response.status_code == 200:
			return "Toilet flush successfully processed"
		else:
			return "Error: " + self._errorFormatter.formatErrorCode(response)
