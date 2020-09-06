#! /usr/bin/env python3
# Image_Site_Downloader.pyw
'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that has
a search feature.

'''

import requests, sys, bs4, os, pprint
from selenium import webdriver #need selenium b/c html containing img info appears from JS

#set cwd
cwd = '/home/xubuntu/Desktop/Automate The Boring Stuff/Web Scraping Chapter/Image_Site_Downloader/'
os.chdir(cwd)
#make a folder for images
os.makedirs(cwd + 'downloadedImages/', exist_ok=True)

#form a link using the website's URI format
home = 'https://www.flickr.com'
path = '/search/?text='
print('Enter your image search term with space between each word:')
search_term_string = input() #enter search term on terminal
link = home + path + search_term_string

#request link
browser = webdriver.Firefox()
browser.get(link)

#loop to follow each img result link and download its img file 
numDownload = 10
for i in range(numDownload):
    #create WebElements via Selenium CSS Selector
    img_elem = browser.find_elements_by_css_selector('.photo-list-photo-interaction .interaction-bar .text .title')
    pprint.pprint('img_elem:' + str(img_elem))
    to_img_link = img_elem[i].get_attribute('href')
    pprint.pprint('Link from Selenium: ' + to_img_link)

    #request the link with the proper CSS selector
    res = requests.get(to_img_link)
    res.raise_for_status()

    #create bs4 object
    flickrSoup = bs4.BeautifulSoup(res.text,'lxml')
    imgElem = flickrSoup.select('.main-photo')
    pprint.pprint(imgElem)
    for_img_link = imgElem[1].attrs['src']
    pprint.pprint(for_img_link)
    img_link = 'https:' + for_img_link
    pprint.pprint(img_link)

    #link to the img file
    res = requests.get(img_link)
    res.raise_for_status()

    #download the img file
    img_file = open(os.path.join('downloadedImages', os.path.basename(img_link)), 'wb')
    print('Downloading image...')
    for chunk in res.iter_content(100000):
        img_file.write(chunk)
    img_file.close()
    print('Image downloaded')

print('Finished downloading all images')
