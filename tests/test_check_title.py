import pytest

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
base_url = "https://www.ebay.com/"


@pytest.mark.smoketest
def test_check_title(browser):
    # navigate to ebay.com home page
    browser.get(base_url)
    # verify website title is ebay.com
    assert browser.title == expected_title
