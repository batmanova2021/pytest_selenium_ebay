import pytest

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
base_url = "https://www.ebay.com/"
my_title = "macbook pro | eBay"


@pytest.mark.parametrize("item", [
    "new macbook",
    "Apple MacBook",
    "Apple MacBook Pro 15 inch"])
@pytest.mark.regressiontest
def test_search_macbook_pro(browser, item):
    browser.get(base_url)
    assert browser.title == expected_title
    browser.find_element_by_id("gh-ac").send_keys("macbook pro")
    browser.find_element_by_id("gh-btn").click()
    assert browser.title == my_title

    browser.find_element_by_id("gh-ac").clear()
    browser.find_element_by_id("gh-ac").send_keys(item)
    browser.find_element_by_id("gh-btn").click()
    assert browser.title == item + " | eBay"

