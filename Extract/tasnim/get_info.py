from bs4 import BeautifulSoup
import os, fnmatch
import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
import requests
import glob
import os


def get_info(url : str) -> dict: 
  