# Run queries on list of applicants

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import os
import time
import fnmatch
import pickle
import sys

## URL's of the websites
url1 = 'https://exclusions.oig.hhs.gov/default.aspx?AspxAutoDetectCookieSupport=1'
url2 = 'https://www.nsopw.gov/'
url3 = 'https://sam.gov/search/?index=ex&pageSize=25&page=1&sort=null&sfm%5Bstatus%5D%5Bis_active%5D=true&sfm%5Bstatus%5D%5Bis_inactive%5D=null'
url4 = 'https://www.instantofac.com/search.php'
url5 = 'https://health.mil/About-MHS/OASDHA/Defense-Health-Agency/DHA-Office-of-the-Inspector-General/Fraud-and-Abuse/Excluded-Providers'


# Define the webdriver options
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": os.getcwd(),  # Define default directory
"download.prompt_for_download": False,  # To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True  # To download PDF files
})

# Open and read the txt file
with open('names.txt', 'r') as f:
    queries = f.readlines()

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)


# Function to parse names in text file and put them in an array
def parse_names(names):
    parsed_data = []

    for name in names:
        name = name.strip()
        components = name.split()

        if not name:
            continue
        
        # Default values
        first_name, middle_name, last_name = None, None, None
        
        for component in components:
            idx, name = component.split(":")
            
            if idx == "1":
                first_name = name
            elif idx == "2":
                middle_name = name
            elif idx == "3":
                last_name = name
        
        # Append the tuple to the parsed_data list
        parsed_data.append((first_name, middle_name, last_name))

    #for entry in parsed_data:
    #    print("First name:", entry[0], "| Middle name:", entry[1], "| Last name:", entry[2])
    
    return parsed_data

# Create a list of names based on the text file
name_list = parse_names(queries)

#for entry in name_list:
#        print("First name:", entry[0], "| Middle name:", entry[1], "| Last name:", entry[2])

driver.get(url1)

