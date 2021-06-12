import pytest

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
base_url = "https://www.ebay.com/"
motors_title = "eBay Motors: Auto Parts and Vehicles | eBay"


@pytest.mark.smoketest
def test_verify_title(browser):
    browser.get(base_url)
    assert browser.title == expected_title
    browser.find_element_by_link_text("Motors").click()
    assert browser.title == motors_title
