import pytest
from selenium.webdriver.support.select import Select

base_url = "https://www.ebay.com/"


@pytest.mark.parametrize("make , model , zip , condition ",
                         [
                             ("BMW", "1800", "22031", "New & Used"),
                             ("Acura", "CL", "22031", "Used"),
                             ("Buick", "GS", "22031", "Used")])
@pytest.mark.regressiontest2
def test_parametrize_search_cars(browser, make, model, zip, condition):
    browser.get(base_url)
    browser.find_element_by_link_text("Motors").click()
    browser.find_element_by_xpath("//select[@aria-label='All Makes']").click()
    dropdown_makes = Select(browser.find_element_by_xpath("//select[@aria-label='All Makes']"))
    dropdown_makes.select_by_visible_text(make)
    dropdown_model = Select(browser.find_element_by_xpath("//select[@aria-label='All Models']"))
    dropdown_model.select_by_visible_text(model)
    browser.find_element_by_name("_stpos").clear()
    browser.find_element_by_name("_stpos").send_keys(zip)
    dropdown_condition = Select(browser.find_element_by_xpath("//select[@aria-label='Condition']"))
    dropdown_condition.select_by_visible_text(condition)
    browser.find_element_by_xpath("//button[text()='Find Vehicle']").click()
    assert browser.title == make.lower() + " " + model.lower() + " in Cars & Trucks | eBay"
