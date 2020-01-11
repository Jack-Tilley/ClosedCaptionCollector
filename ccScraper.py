# Jack Tilley
# January 2020
# This code collects the closed captions from any youtube video
# This could be used for rapidly searching videos for keywords or quotes

from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.options import Options


class ClosedCaptionCollector: # class to gather and display the closed captions
    def __init__(self,url, PATHTODRIVER):
        self.url = url
        self.PATHTODRIVER = PATHTODRIVER
        self.transcript = []
        self.timestamps = []

    def scrape(self): # scrapes the transcript from youtube using selenium clicks and bs4
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options = selenium.webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('user-agent={0}'.format(user_agent))

        url = self.url
        path = self.PATHTODRIVER

        driver = webdriver.Chrome(path, chrome_options=options)
        driver.set_window_size(1440, 900)
        driver.get(url)
        time.sleep(1)

        options_button = driver.find_elements_by_xpath("//button[@aria-label='More actions']")[0]
        options_button.click()
        time.sleep(1)

        transcript_button = \
        driver.find_elements_by_xpath("//paper-item[@class='style-scope ytd-menu-service-item-renderer']")[0]
        transcript_button.click()
        time.sleep(1)

        innerHTML = driver.execute_script("return document.body.innerHTML")
        time.sleep(1)

        soup = BeautifulSoup(innerHTML, "html.parser")
        soupscope = soup.find("div", attrs={"id": "body", "class": "style-scope ytd-transcript-renderer"})


        transcript_content = soupscope.find_all("div",
                                                attrs={"class": "cue-group style-scope ytd-transcript-body-renderer"})

        driver.close()

        return transcript_content

    def create_transcript(self): # calls scrape and creates the transcript
        transcript_content = self.scrape()

        for line in transcript_content:
            output = line.text
            output = ' '.join(output.split())
            self.transcript.append(output)

    def get_transcript(self): # used to return the transcript in list form
        return self.transcript

    def print_transcript(self): # used to print the transcript  in readable form
        for line in self.transcript:
            print(line)
