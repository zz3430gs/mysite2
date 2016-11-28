import wikipedia
from bs4 import BeautifulSoup
import urllib


def search():
    query = ""
    wikipedia.summary(query, sentences=10)


def summary():
    #Just a substitute nothing here yet
    return False