# Image-Site-Downloader

This script was built as practice for incorporating python modules that would be able to go to a photo-sharing site like Flickr, search for a category of photos, and then download all the resulting images. The idea is that a script like this can be written to work with any photo site that hasa search feature.

General Process:
1. The script imports the modules it requires. The goal was to practice using Selenium and BeautifulSoup, so these are the important modules to be noted.
2. The current working directory is setup and creates a folder to download images to.
3. With some analysis of the image search website, the general format used for the URI can be found such that a search can be automatically made by changing the URI as needed, i.e. https://www.flickr.com/search/?text=<insert search term here>. With this, the user can input their search term on the terminal and let python handle the search and download.
4. For a site like Flickr, it turns out that CSS elements are required that only appear when the site loads its javascript. These elements are required to make the searches possible. Selenium is used to request Firefox to open the desired link such that the javascript can load. Using other modules alone to request a search for CSS elements will not work, therefore requiring a module like Selenium. 
5. Now that the sites have been loaded via the selenium webdriver, as they might be loaded for a normal user on their browser, the BeautifulSoup module can be leveraged to retrieve the necessary CSS elements containing information on the available images and the links to their files.
6. The requests module can be used now to request the image file link. 
7. These steps can be iterated for the number of the desired images for download using a for loop. The script then tells the user it has finished downloading all the images. 
