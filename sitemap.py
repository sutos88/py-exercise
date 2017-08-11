import csv
import re
import sys
import pandas as pd
from datetime import datetime

from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
inputLocation = "./Input/"
outputLocation = "./Output/"
listToFile = []
def ConvertDate():

    date = str(datetime.now())
    date = date.split(".")[0]
    date = re.sub(" ", "_", date)
    date = re.sub("\.", "_", date)
    date = re.sub(":", "-", date)

    return date

def ConvertUrl(Url):

    Url = re.sub("http://", "_", Url)
    Url = re.sub(".", "_", Url)

    return Url

def site_crawler(homeUrl, actualUrl, depth, depthCount):



    soup = BeautifulSoup(driver.page_source, "html.parser")

    linkList = soup.find_all("a")

    if len(linkList) == 0:
        return

    for link in linkList:
        linkurl = link.get('href')
        if linkurl.startswith('/'):
            listToFile.append(linkurl + "," + homeUrl + "," + str(depthCount+1) + "\n")
            print(linkurl + "," + homeUrl + "," + str(depthCount+1) + "\n")
            try:
                driver.find_element_by_link_text(link.text).click()
            except:
                print("Unable to click: " + linkurl)
                continue
            driver.implicitly_wait(1)
            if depthCount+1 < depth:
                site_crawler(homeUrl, linkurl, depth, depthCount+1)





def main(argv):


    inputFile = open('C:\PycharmProjects\sitemap\Input\input.csv', encoding='utf-8', mode='r', newline='')
    inputReader = csv.DictReader(inputFile)



    for index, row in enumerate(inputReader):
        url = row['Url']
        depth = int(row['Depth'])
        outputFile = open(outputLocation + ConvertDate() + "-" + ConvertUrl(url) + ".csv", encoding='utf-8', mode='w')
        outputFile.write("Actual Page Url,Previous page Url,Actual depth\n")
        depthCount = 1
        driver.get(url)
        driver.maximize_window()
        site_crawler(url, url, depth, depthCount)
        outputFile.write(listToFile)
        del listToFile


    print("It's done.")
    driver.close()
    inputFile.close()                                                                       # Close the input and output file
    outputFile.close()

if __name__ == "__main__":
    main(sys.argv)