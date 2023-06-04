
# Asyncio really shines when it comes to I/O-bound tasks, like making requests to a server. Let's see how you can use it to speed up such tasks.

# Create a script named challenge.py that accomplishes the following tasks:

# First, install the aiohttp and beautifulsoup4 libraries if you haven't already. These are not part of the Python standard library. You can install them using pip:

# shell
# Copy code
# pip install aiohttp beautifulsoup4
# Create a coroutine named fetch_page that accepts an argument url (a string). The coroutine should use aiohttp to make a GET request to the url, then use BeautifulSoup to parse the HTML response and find the title tag (<title>). It should return the text content of the title tag.

# Create a main function named main, which will be your entry point. In this function, use asyncio to run several instances of fetch_page concurrently, one for each of the following URLs:

# plaintext
# Copy code
# https://www.wikipedia.org/
# https://www.python.org/
# https://www.openai.com/
# The main function should print the results of the coroutines as they arrive, each one formatted as "Page title: <title>" (replace <title> with the actual title).

# Test Case:

# You should be able to run this script from the command line using python challenge.py. The script should print something like:

# plaintext
# Copy code
# Page title: Wikipedia
# Page title: Welcome to Python.org
# Page title: OpenAI
from collections import namedtuple
import asyncio

import aiohttp
from bs4 import BeautifulSoup

Page = namedtuple("Page", ["title"])

async def fetch_page(url: str, session: aiohttp.ClientSession) -> Page:
    async with session.get(url) as response:
        text = await response.text()
        return Page(BeautifulSoup(text, features="html.parser").title.string)


async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch_page(url, session)
                                       for url in [
                                        "https://www.wikipedia.org/",
                                       "https://www.python.org/",
                                       "https://www.openai.com/"]))

    for result in results:
        print(f"Page title: {result.title}")

asyncio.run(main())
