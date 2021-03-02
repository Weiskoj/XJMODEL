
import sqlite3
from bs4 import BeautifulSoup
import os
import requests

def getTempest(zip = 66952):
    url = "https://www.autotempest.com/results?"
    payload = {"zip": zip, "make": "jeep","model": "cherokee", "minyear": 1983,"maxyear": 2001}
    rslt = requests.get(url, params = payload)
    soup = BeautifulSoup(rslt.content, "html.parser")
    ebay_listings = soup.find("section", id = "eb-results")
    cars_listings = soup.find("section", id = "cm-results")
    truecar_listings = soup.find("section", id = "tc-results")
    craigslist_listings = soup.find("section", id = "st-results")

    return {"ebay_data": ebay_listings, "cars_data": cars_listings, "truecar_data": truecar_listings, "craigslist_data": craigslist_listings}

def processEbay(data):
    # TODO: finish
    step1 = data.find("section", class_ = "results-list") # Grabs HTML section containing e-bay listings.
    print(step1.find(class_ = "results-target"))


def processCars(listings):
    #TODO: finish processCars
    print("TODO: finish processCars")
def processTrueCar(listings):
    # TODO: finish
    print("TODO: finish processTrueCar")
def processCraigsList(listings):
    # TODO: finish
    print("TODO: finish processCraigsList")

def processing_handler(unp_data_dict):

    print("processing Ebay listings...")
    processEbay(unp_data_dict["ebay_data"])
    print("done")
    print("processing Cars.com listings...")
    processCars(unp_data_dict["cars_data"])
    print("done")
    print("processing TrueCar listings...")
    processTrueCar(unp_data_dict["truecar_data"])
    print("done")
    print("processing CraigsList listings...")
    print("done")
    processCraigsList(unp_data_dict["craigslist_data"])


def main():
    #zip = input("Please input the ZIP code you would like to search near *REQUIRED* :  ")
    #setUpConnection()
    unp_data = getTempest()
    processEbay(unp_data["ebay_data"])

main()