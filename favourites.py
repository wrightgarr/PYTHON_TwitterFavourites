import tweepy
import json
import requests
from requests_oauthlib import OAuth1
from config import consumer_key,consumer_secret,access_token,access_token_secret, screen_name

# test connection/verify credentials
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
requests.get(url, auth=auth)


# call api/GET 200 most recent favourites
def call_api():
	response = requests.get(f'https://api.twitter.com/1.1/favorites/list.json?count=200&screen_name={screen_name}', auth=auth)
	return response.json()


# using the response of the GET request, populate an array of tweet IDs
def favourites_list(response_json):
	"""
	accepts: response.json() of twitter API favourites GET request
	"""
	favourites_list = []
	for tweet in response_json:
		favourites_list.append(tweet['id'])
	return favourites_list


# remove favourite
def destroy_favourite(favs_list):
	while len(favs_list) > 0:
		tweet_id = favs_list[0]
		destroy_fav = requests.post(f'https://api.twitter.com/1.1/favorites/destroy.json?id={tweet_id}', auth=auth)
		destroy_fav
		favs_list.remove(tweet_id)
		print(f'Favourites remaining: {len(favs_list)}')


if __name__ == '__main__':
	favs = favourites_list(call_api())
	print(favs)
	destroy_favourite(favs)
