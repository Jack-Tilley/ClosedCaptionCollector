# Jack Tilley
# January 2020
# Example file on how to use ccScraper.py

from ccScraper import ClosedCaptionCollector

url = "https://www.youtube.com/watch?v=k6U-i4gXkLM" # this is the youtube url that you want to get ccs from

path = "path/to/your/chromedriver" # to install chromedriver or with help setting up selenium, follow this link:
# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver

cc = ClosedCaptionCollector(url, path) # creates a instance of a closed caption transcipt object

cc.create_transcript() # does the grunt work of gathering the closed captions

cc.print_transcript() # prints transcript in human readable form

print(cc.get_transcript()) # prints transcript in list form