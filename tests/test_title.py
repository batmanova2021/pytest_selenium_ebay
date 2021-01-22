import pytest
from selenium import webdriver

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
base_url = "https://www.ebay.com/"


@pytest.mark.anna6
def test_title(browser):
    # navigate to ebay.com home page
    browser.get(base_url)
    # verify website title is ebay.com
    assert browser.title == expected_title

