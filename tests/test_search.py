import pytest

expected_title =  "Electronics, Cars, Fashion, Collectibles & More | eBay"
base_url = "https://www.ebay.com/"
search_title = "glasses | eBay"

@pytest.mark.regressiontest
def test_search_glasses(browser):
    browser.get(base_url)
    assert browser.title == expected_title
    # locate search field element
    search_field = browser.find_element_by_id("gh-ac")
    # enter "glasses" in the search field
    search_field.send_keys("glasses")
    # locate search button
    search_button = browser.find_element_by_id("gh-btn")
    # click on 'Search' button
    search_button.click()
    # verify actual page title matches expected page title
    assert browser.title == search_title