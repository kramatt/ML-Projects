# Practice using Selenium for web scraping with headless browser
# Following tutorial at https://realpython.com/modern-web-automation-with-python-and-selenium/

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.set_headless()
assert opts.headless

#browser = Chrome(options=opts)
#browser.get('https://duckduckgo.com')
