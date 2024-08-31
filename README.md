# Immobiliare .it Analyser
This repo is an example of how you can make data accessible with Python and LLMs for FREE.

## Let me exaplain
Immobiliare is a seamless site for finding houses for sell and rent. \
It has a lot filter and settings, making the research the most specific as possible. 

Yet it doesn't have some filters I was personally searching for, number of bedrooms, rent contract types and students-only flag.

## How it works

- You define your basic filter on Immobiliare site
- You copy the url and paste it in settings.json file
- Browse the properly filtered results after running the tool a few minutes

## So what does this tool do?
This tool acquire all search results, collect and analyze them in order to open the links properly filtered in your browser.

- It makes a request to Immobiliare search query (previously built on Immobiliare website).
- Foreach result it makes a request to it in order to get the house's description. 
- Now instead of using regex or other so fancy yet shitty things,
- it calls Llama 3.1 405B via API to analyze the house details and answer some question instead of me.
- After waiting for all info to be collected and processed, it filters by sending all answers to Llama.

Finally, it opens all filtered results. 

## Setup
You need to setup a few things, but just once.

#### LLM
As I said, Llama 3.1 is used, but you don't need to hosts nor pays it. \
I integrated [Akash Chat](https://chat.akash.network) Api for FREE, as it is actually free and offered from [Akash Cloud](https://akash.network/).

1. Go to https://chatapi.akash.network/
2. Click Get Started
3. Fill the form
4. Click Generate Api Key
5. Copy it
6. Paste it in `"api"` field in settings.json file

#### Browser
1. Locate your Firefox or Chrome browser executable
2. If you don't know, just ask Akash Chat :)
3. Copy the path
4. Paste it in `"firefox_path"` or `"chrome_path"` field in settings.json file

#### Immobiliare link
1. Go to https://www.immobiliare.it/
2. Select Affitta / Rent
3. Insert every filter you need (such as districts, price range,  ecc)
4. Copy the url from the browser
5. Paste it in `"link"` field in settings.json file

#### Python Package
1. Open a terminal
2. Run `pip install -r -U requirements.txt`

## Run
1. Open a terminal inside the script's folder
2. Run `python main.py`
