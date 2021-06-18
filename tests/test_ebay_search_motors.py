import pytest
from selenium.webdriver.support.wait import WebDriverWait

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
base_url = "https://www.ebay.com/"
my_title = "macbook pro | eBay"


@pytest.mark.regressiontest
def test_ebay_search_motors(browser):
    browser.get(base_url)
    assert browser.title == expected_title
    browser.find_element_by_link_text("Motors").click()
    browser.find_element_by_xpath("//select[@name='Make'][@aria-label='All Makes']")
    make = WebDriverWait (browser,10).until(lambda x : x.find_element_by_xpath("//select[@name='Make'][@aria-label='All Makes']"))
    make.click()
    make_name = WebDriverWait (browser,10).until(lambda x : x.find_element_by_xpath("//select/option[@value='Aston Martin']"))
    make_name.click()
