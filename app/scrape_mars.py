
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import time
import re


def mars_news(browser):
    url = "https://mars.nasa.gov.news/"
    browser.visit(url)

# Get first list itemwait hold a second if not immediately present
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=0.5)

    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        new_title = slide_elem.find("div", class_="content_title").get_text()
        news_p = slide_elem.find(
            "div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    return


def featured_image(browser):
    return


def hemisphere(browser):
    return


def twitter_weather(browser):
    return


def scrape_hemispher(html_text):

    return


def mars_facts():
    try:
        df = pd.read_html("https://space-facts.com/mars/")[0]
    except BaseException:
        return None
        df.columns = ["description", "value"]
        df.set_index("description", inplace=True)
    return df.to_html(classes="table table-striped")


if __name__ == "__main__":
    print(scrape_all())


def scrape_all():
    executable_path = {"executable_path": "chromedrive.exe"}
    browser = Browser("chrome", executable_path="chromedriver", headless=False)

    news_title, news_paragraph = mars_news(browser)

    data = {
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    return data
