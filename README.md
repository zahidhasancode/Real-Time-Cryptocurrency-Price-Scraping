# Real-Time-Cryptocurrency-Price-Scraping

This document explains a Python script designed to scrape and display the real-time price of a specific cryptocurrency from a web page. The script uses the requests library to fetch web page content, BeautifulSoup from bs4 for parsing HTML, and a loop to continuously update the price every 5 seconds.

**Overview**

The script targets a specific URL to retrieve the real-time price of the AGC cryptocurrency token from the Coinscan website. It is designed to run indefinitely, fetching and printing the latest price to the console every 5 seconds.

**Dependencies**

requests: For making HTTP requests to fetch the web page.
BeautifulSoup: For parsing the HTML content and navigating the DOM tree to find the price element.
Script Explanation
**Fetching Web Page Content**

The script defines a function get_agc_price() that sends a GET request to the specified URL. It uses requests.get(url) to retrieve the page content.

**Parsing HTML**

Upon receiving a successful response, the function parses the HTML content using BeautifulSoup(response.text, 'html.parser').

**Extracting the Price**

The script navigates through the HTML structure to locate the price of the cryptocurrency. It identifies the correct div and span elements by their class names to find where the price is located.

**Error Handling**

**The script checks for errors at each step:**


If the HTTP request fails, it prints a message indicating the failure.
If the necessary HTML elements are not found, it informs the user that the specific elements could not be located.
**Continuous Price Updates**

The main part of the script enters an infinite loop, calling get_agc_price() every 5 seconds. It prints the current price if successful or an error message otherwise.

**Usage**

To use the script, simply run it in a Python environment. Ensure you have the requests and bs4 libraries installed. The script does not require any input and will start displaying the price information immediately, updating every 5 seconds until manually stopped.

**Limitations**

This script is designed for educational purposes and demonstrates basic web scraping techniques. The structure of web pages can change, which may require updates to the script to continue functioning correctly.

