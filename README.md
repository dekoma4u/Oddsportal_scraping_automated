# Scraper for Counter strike odds from oddsportal
Uploading Screen Recording 2022-09-11 at 22.32.48.mov…
## How to install chrome driver:
Download the chrome driver on your laptop. From your terminal, go to the location of the chrome driver and run this code to grant it permission to run on your computer. spctl --add --label 'Approved' chromedriver
copy the path and paste it into line 10 as you replace my own path.

## Must do
Create two folders with name games and odds in the root directory. These are where the results of the scraping are stored in csv and txt formats, other wise, you might need to change the file location in lines 21, 29, and 71 respectively for both scraper.py and scraper2.py.

## How it works:
The codes take care of the cookies and iterate through games and go within a particular game and scrape through the respective bookmakers' odds and score line and append them in CSV and text files.
It does that for all the games. The matches are stored in a text file alongside the score lines.

### NB: The data can further be cleaned according to respective needs.
