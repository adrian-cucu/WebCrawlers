import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import urlunparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import sys
import json
import re
from tempfile import NamedTemporaryFile
import shutil
import csv


class CsvManager:
    def __init__(self, file_name, fields):
        self.file_name = file_name
        self.fields = fields
        self.updated_rows_id = set()
        self.csv_file = None
        self.temp_file = None
        self.reader = None
        self.writer = None

    def open_file(self):
        self.csv_file = open(self.file_name, 'r')
        self.temp_file = NamedTemporaryFile(mode='w', delete=False)

        self.reader = csv.DictReader(self.csv_file, fieldnames=self.fields)
        self.writer = csv.DictWriter(self.temp_file, fieldnames=self.fields)

    def done(self):
        if self.csv_file is not None:
            self.csv_file.seek(0)
            for row in self.reader:
                if row['ID'] in self.updated_rows_id:
                    print("row: ", row, " already was updated")
                else:
                    self.writer.writerow(row)
            self.csv_file.close()

        if self.temp_file is not None:
            shutil.move(self.temp_file.name, self.file_name)

    def update_row(self, row_dict):
        for row in self.reader:
            if row['ID'] == str(row_dict['ID']):
                print("Updating row", row)
                self.updated_rows_id.add(row['ID'])
                self.writer.writerow(row_dict)
                return

        print("Ading a new row ", row_dict)
        self.writer.writerow(row_dict)


filename = 'my.csv'
fields = ['ID', 'Name', 'Course', 'Year']
csv_manager = CsvManager(filename, fields)

update_row = dict()
update_row["ID"] = 1
update_row["Name"] = "John"
update_row["Course"] = "Math2"
update_row["Year"] = 2026

csv_manager.open_file()
csv_manager.update_row(update_row)

update_row = dict()
update_row["ID"] = 2
update_row["Name"] = "Leo"
update_row["Course"] = "physics-sport"
update_row["Year"] = 2022

csv_manager.update_row(update_row)

csv_manager.done()

sys.exit(0)

# with open(filename, 'r') as csvfile, tempfile:
#     reader = csv.DictReader(csvfile, fieldnames=fields)
#     writer = csv.DictWriter(tempfile, fieldnames=fields)
#     for row in reader:
#         print(row)
#         if row['ID'] == str(update_row['ID']):
#             print('updating row', row['ID'])
#         #     row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
#         # row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
#         # writer.writerow(row)
#
# # shutil.move(tempfile.name, filename)


sys.exit(0)
t1 = time.time()
# r = requests.post(url="https://aukcje.ideagetin.pl/aukcja/9407/scania-touring-hd-51-osobowy/")
r = requests.get(url="https://aukcje.ideagetin.pl/zdjecia/9407/autobus-scania-touring-hd-51-osobowy/")

soup = BeautifulSoup(r.content, 'html.parser')
for a in soup.find("div", {"class": "bottom-images"}).findAll("a"):
    print(a.get("href"))

print("%d" % (time.time() - t1))

sys.exit(0)

chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
driver = webdriver.Chrome(executable_path=os.path.abspath("/bin/chromedriver"), chrome_options=chrome_options)

t1 = time.time()

# driver.get("https://aukcje.pkoleasing.pl/en/auctions/details/volvo-xc60-combi/ge6po7a1")
# driver.get("https://aukcje.pkoleasing.pl/en/auctions/details/volvo-xc60-combi/ge6po7a1")
# driver.get("https://aukcje.pkoleasing.pl/en/auctions/details/volvo-xc60-combi/ge6po7a1")
# driver.get("https://aukcje.pkoleasing.pl/en/auctions/details/volvo-xc60-combi/ge6po7a1")
# driver.get("https://aukcje.pkoleasing.pl/en/auctions/details/volvo-xc60-combi/ge6po7a1")
# driver.get("https://aukcje.pkoleasing.pl/en/auctions/details/volvo-xc60-combi/ge6po7a1")
driver.get("https://aukcje.ideagetin.pl/aukcja/9407/scania-touring-hd-51-osobowy/")

# driver.execute_script()

html = requests.get("https://aukcje.ideagetin.pl/aukcja/9407/scania-touring-hd-51-osobowy/")
# print(html.text)

with open("page.txt", "w", encoding="utf-8") as f:
    f.write(html.text)

sys.exit(0)
# driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html.text))
# print(json.dumps(html.content))
# driver.execute_script("document.write({})".format(re.escape(html.content)))
# driver.execute_script("document.write('{}')".format(re.escape(html.text)))

# print(driver.current_url)

print("%d" % (time.time() - t1))

# print(driver.find_element_by_class_name("price").find_element_by_xpath("//span[@class='ng-binding']").text)
# print(driver.find_element_by_xpath("//a[@class='more-pictures']"))
print(driver.find_element_by_xpath("//a[@class='more-pictures']").click())

wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='popup-overlay']")))
#
# images_div = driver.find_element_by_xpath("//div[@class='bottom-images']")
# for bottom_image in images_div.find_elements_by_tag_name("a"):
#     print(bottom_image.get_attribute("href"))

print("%d" % (time.time() - t1))

# magnifying_glass = driver.find_element_by_id("js-open-icon")
# if magnifying_glass.is_displayed():
#   magnifying_glass.click()
# else:
#   menu_button = driver.find_element_by_css_selector(".menu-trigger.local")
#   menu_button.click()
#
# search_field = driver.find_element_by_id("site-search")
# search_field.clear()
# search_field.send_keys("Olabode")
# search_field.send_keys(Keys.RETURN)
# assert "Looking Back at Android Securi
