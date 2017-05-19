# Fresh Tomatoes

Fresh Tomatoes will gather the biggest film releases in theaters and display them on a webpage along with their respective trailers on youtube.


## Install

Can be installed by cloning from github repository.

`git clone https://github.com/jakec-github/ud036_StarterCode.git`


## Usage

To run Fresh Tomatoes run the run.py module using python 3 eg:

`python3 run.py`

Before running the program please check the requirements section.

Progress will be printed to the console.

## Requirements

This program requires the python module [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/). This module is used to scrape data from imdb.com This can be installed using pip.

`pip install beautifulsoup4`
or
`pip3 install beautifulsoup4`

## Issues

The application will make several web requests to get the required movie data. This means there is a short wait between starting the program and the web page opening. This wait can be reduced by altering the number of movies gathered in the scraper module.
