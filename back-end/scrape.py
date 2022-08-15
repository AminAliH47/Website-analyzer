import json
from time import sleep
import requests
from requests.auth import HTTPBasicAuth
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException

options = Options()

options.page_load_strategy = 'none'
options.add_argument("--headless")

driver = Chrome(service=Service("/home/aminali/Documents/chromedriver"), options=options)


def get_backlinks():
    """
    This method scrape the backlinks' data with selenium

    :return: Backlinks data Includes number_of_backlinks, referring_domains,
    total_no_follow_links and indexed_pages_in_google
    """

    # Get backlinks URL
    try:
        driver.get("https://lxrmarketplace.com/seo-inbound-link-checker-tool.html")
    except TimeoutException:
        pass

    # find search bar element
    sleep(1)
    search_bar = driver.find_element(By.ID, "url")

    url = 'https://shahdin.com/'
    # Pass URL to search bar
    search_bar.send_keys(url)
    search_bar.send_keys(Keys.RETURN)

    # Get number of backlinks
    try:
        number_of_backlinks = driver.find_element(
            By.XPATH,
            '//*[@id="resultSection"]/div[2]/div[1]/div[1]/h3'
        ).text
    except NoSuchElementException:
        number_of_backlinks = None
    except ElementNotInteractableException:
        number_of_backlinks = None

    # Get referring domains
    try:
        referring_domains = driver.find_element(
            By.XPATH,
            '//*[@id="resultSection"]/div[2]/div[2]/div[1]/h3'
        ).text
    except NoSuchElementException:
        referring_domains = None
    except ElementNotInteractableException:
        referring_domains = None

    # Get total no follow links
    try:
        total_no_follow_links = driver.find_element(
            By.XPATH,
            '//*[@id="resultSection"]/div[2]/div[3]/div[1]/h3'
        ).text
    except NoSuchElementException:
        total_no_follow_links = None
    except ElementNotInteractableException:
        total_no_follow_links = None

    # Get indexed pages in google
    try:
        indexed_pages_in_google = driver.find_element(
            By.XPATH,
            '//*[@id="resultSection"]/div[2]/div[6]/div[1]/h3'
        ).text
    except NoSuchElementException:
        indexed_pages_in_google = None
    except ElementNotInteractableException:
        indexed_pages_in_google = None

    # Save data in dictionary
    inbound_links = {
        "number_of_backlinks": number_of_backlinks,
        "referring_domains": referring_domains,
        "total_no_follow_links": total_no_follow_links,
        "indexed_pages_in_google": indexed_pages_in_google,
    }
    return inbound_links


def get_gtmetrix():
    """
    This method gets GTmetrix data from the API and create JSON
    with our required data.

    API 1: Gets Pagespeed score, Yslow score
    API 2: Gets GTmetrix grade, performance score, structure score, fully_loaded_time

    :return: JSON with GTmetrix data
    """
    # Create raw body data for API 1
    _data_1 = {
        "url": "https://mashadsanat.ir/"
    }
    # Authentication and Create new GTmetrix test for API 1
    _raw_response_1 = requests.post(
        "https://gtmetrix.com/api/0.1/test", data=_data_1,
        auth=HTTPBasicAuth("fonege1411@lodores.com", "3924603839ec7587fc2192b427ce7e43")
    ).json()

    # get report url for API 1
    _result_url_1 = _raw_response_1['poll_state_url']

    # Wait for GTmetrix to generate API 1 Report
    while True:
        sleep(9)
        api1 = requests.get(
            _result_url_1,
            auth=HTTPBasicAuth("fonege1411@lodores.com", "3924603839ec7587fc2192b427ce7e43")
        ).json()

        api1 = api1['results']
        try:
            api1['pagespeed_score']
        except KeyError:
            pass
        else:
            break

    # Create raw body data for API 2
    _data_2 = """
    {
      "data": {
        "type": "test",
        "attributes": {
          "url": "https://mashadsanat.ir/"
        }
      }
    }
    """
    # Set request headers for API 2
    _headers_2 = {
        "Content-Type": "application/vnd.api+json"
    }
    # Authentication and Create new GTmetrix test for API 2
    _raw_response_2 = requests.post(
        "https://gtmetrix.com/api/2.0/tests", headers=_headers_2, data=_data_2,
        auth=HTTPBasicAuth("3924603839ec7587fc2192b427ce7e43", "")
    ).json()

    # get report url for API 2
    _result_url_2 = _raw_response_2['links']['self']

    # Wait for GTmetrix to generate API 2 Report
    while True:
        sleep(9)
        api2 = requests.get(
            _result_url_2,
            auth=HTTPBasicAuth("3924603839ec7587fc2192b427ce7e43", "")
        ).json()

        api2 = api2['data']['attributes']
        try:
            api2['performance_score']
        except KeyError:
            pass
        else:
            break

    data = {
        "pagespeed_score": api1['pagespeed_score'],
        "yslow_score": api1['yslow_score'],
        "gtmetrix_grade": api2['gtmetrix_grade'],
        "performance_score": api2['performance_score'],
        "structure_score": api2['structure_score'],
        "fully_loaded_time": api2['fully_loaded_time'],
    }
    print(data)
    return data


get_gtmetrix()

# Close driver after scrape page
driver.close()
