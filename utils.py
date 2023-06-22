import json

# function to get the url from the secrets.json file
def get_url():
    with open('secrets.json') as f:
        data = json.load(f)
        url = data['url']
        return url
