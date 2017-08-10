import csv
import re
import sys
from datetime import datetime

from selenium import webdriver
from bs4 import BeautifulSoup

inputLocation = "./Input/"
outputLocation = "./Output/"
driver = webdriver.Chrome()

def ConvertDate():

    date = str(datetime.now())
    date = date.split(".")[0]
    date = re.sub(" ", "_", date)
    date = re.sub("\.", "_", date)
    date = re.sub(":", "-", date)

    return date

def sitemap_crawler(homeUrl, actualUrl, depth, depthCount):

    actualWebElements = driver.find_elements_by_tag_name("a")

    if len(actualWebElements) == 0:
        return

    soup = BeautifulSoup


def main(argv):

    inputFile = open(inputLocation + "input.csv", encoding='utf-8', mode='r', newline='')
    inputReader = csv.DictReader(inputFile)

    outputFile = open(outputLocation + ConvertDate() + ".csv", encoding='utf-8', mode='w')
    outputFile.write("URL,User,Time\n")

    for index, row in enumerate(inputReader):
        url = row['Url']
        depth = row['Depth']
        depthCount = 1

        driver.get(url)
        driver.maximize_window()

    sitemap_crawler(url, url, depth, depthCount)



if __name__ == "__main__":
    main(sys.argv)