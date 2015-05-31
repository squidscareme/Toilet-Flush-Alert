#!/usr/bin/python
from TurdTrackerFacebookFeedPost import TurdTrackerFacebookFeedPost

'''Entry point for the application'''
def main():
	facebookFeedPost = TurdTrackerFacebookFeedPost()
	return facebookFeedPost.informFacebookOfToiletFlush()
	
if __name__ == "__main__":
    # execute only if run as a script
    main()