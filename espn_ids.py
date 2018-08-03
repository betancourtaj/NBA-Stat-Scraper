from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import requests

class Espn_Scrape(object):
	"""Class that allows you to put in the date by year, month, and day then scrapes espn for the game_ids for that date."""

	def __init__(self, year, month, day):
		
		self.year = year
		self.month = month
		self.day = day

		self.url = f"http://www.espn.com/nba/scoreboard/_/date/{year}{month}{day}"

		self.options = Options()
		self.chromedriver = "/Users/alexbetancourt/Downloads/chromedriver"
		self.driver = webdriver.Chrome(self.chromedriver)

		self.driver.get(self.url)
		self.res = self.driver.execute_script("return document.documentElement.outerHTML")
		self.driver.quit()

		self.soup = BeautifulSoup(self.res, 'lxml')

	def find_game_ids(self):
		games = self.soup.find_all(class_="scoreboard basketball final home-winner js-show")

		game_ids = []

		for game in games:
			game_ids.append(game['id'])

		games = self.soup.find_all(class_="scoreboard basketball final away-winner js-show")

		for game in games:
			game_ids.append(game['id'])

		return game_ids

