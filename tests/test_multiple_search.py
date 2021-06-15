import pytest

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
base_url = "https://www.ebay.com/"


@pytest.mark.parametrize("item", [
    "glasses",
    "sunglasses",
    "glasses men",
    "glasses women"])
@pytest.mark.regressiontest
def test_multiple_search(browser, item):
    browser.get(base_url)
    assert browser.title == expected_title
    browser.find_element_by_id("gh-ac").send_keys(item)
    browser.find_element_by_id("gh-btn").click()
    assert browser.title == item + " | eBay"

