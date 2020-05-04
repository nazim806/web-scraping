
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as import pd
import datetime as dt
import time
import re


def scrape_all():
    return


def mars_news(browser):
    return


def featured_image(browser):
    return


def hemisphere(browser):
    return


def twitter_weather(browser):
    return


def scrape_hemispher():
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
