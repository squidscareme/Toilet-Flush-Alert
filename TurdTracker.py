'''
*****************************************************************
Turd TurdTracker

AUTHOR: Jonathan Frazier
DATE: May 31, 2015

DESCRIPTION:
This is a simple program to get my kids interested
in programming. The idea is to call this code from
a raspberry pi when a sensor has detected that the
toilet has flushed.

DEPENDENCIES
Environment Variables:
	TURDTRACKER_FACEBOOK_TOKEN
	TURDTRACKER_FACEBOOK_PAGE_ID
	TURDTRACKER_FACEBOOK_API_VERSION

This code was written using Linux Mint 17.1 Cinnamon 64-bit  
and has been designed to run on Linux.
*****************************************************************
'''

#!/usr/bin/python
from TurdTrackerFacebookFeedPost import TurdTrackerFacebookFeedPost

'''Entry point for the application'''
def main():
	facebookFeedPost = TurdTrackerFacebookFeedPost()
	return facebookFeedPost.informFacebookOfToiletFlush()
	
if __name__ == "__main__":
    # execute only if run as a script
    main()