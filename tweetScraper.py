import configparser
import requests
import os
import json

search_url = "https://api.twitter.com/2/tweets/search/recent"

bearer_token="YOUR TWITTER API"

# Optional params: start_time,end_time,since_id,until_id,next_token,granularity
query_params = {'query': 'Elon Musk', 'lang':'en', }
tweet = False

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "elonTweetScrapper"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    return

if __name__ == "__main__":
    main()
