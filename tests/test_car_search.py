import pytest

from selenium.webdriver.support.select import Select

base_url = "https://www.ebay.com/"


@pytest.mark.regressiontest
def test_car_search(browser):
    browser.get(base_url)
    browser.find_element_by_link_text("Motors").click()
    browser.find_element_by_xpath("//select[@aria-label='All Makes']").click()
    dropdown = Select(browser.find_element_by_xpath("//select[@aria-label='All Makes']"))
    dropdown.select_by_visible_text("BMW")
    browser.find_element_by_xpath("//select[@aria-label='All Models']").click()
    dropdownmodels = Select(browser.find_element_by_xpath("//select[@aria-label='All Models']"))
    dropdownmodels.select_by_visible_text("840Ci")
    browser.find_element_by_name("_stpos").clear()
    browser.find_element_by_name("_stpos").send_keys("22031")
    browser.find_element_by_name("LH_ItemCondition").click()
    dropdowncondition = Select(browser.find_element_by_name("LH_ItemCondition"))
    dropdowncondition.select_by_visible_text("Used")
    browser.find_element_by_xpath("//button[text()='Find Vehicle']").click()
    assert browser.title == "bmw 840ci in Cars & Trucks | eBay"
