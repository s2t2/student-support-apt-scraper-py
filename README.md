


# Web Scraper in Python

Investigating the ability to use Python to parse the contents of a lazy-loaded, nested HTML page.

## Summary of Findings

Parsing the contents of a normal page is easy using the "requests" package and "beautiful soup" Python packages, but issues arise when the page's contents are lazy-loaded after the initial request was made.

So we can use the "selenium" web driver to visit the page and wait for the entire page to load, including the content we care about.

Then after it's loaded, we can use "beautiful soup" as usual to parse the contents.

Success!

## Prerequisites

[Install `chromedriver`](http://chromedriver.chromium.org/getting-started) to enable automated web browsing in Chrome:

```sh
# is chromedriver installed?
chromedriver --version

# install (Mac OS, using homebrew / brew cask):
brew cask install chromedriver

# if the path is messed up, can invoke like so:
/usr/local/bin/chromedriver --version
```

## Setup

Create and activate a virtual environment:

```sh
conda create -n scraper-env
conda activate scraper-env
```

Install package dependencies:

```sh
pip install selenium beautifulsoup4
```

## Usage

```sh
python browsing_starter.py
```
