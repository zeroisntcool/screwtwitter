#!/usr/bin/env python3
import tweepy
import time
import asyncio
from proxybroker import Broker


# Authenticate to Twitter (developer.twitter.com)
api = ""
api_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(api, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def verify():
	try:
		api.verify_credentials()
		print("\n", "	\033[36mTwitter\033[39m bot started ")
		print("	tweeting four tweets per hour ;) ", "\n")
	except:
		print("	Error, no faking idea check your tokens")
verify()
async def tweet(proxies):
    while True:
      try:
        proxy = await proxies.get()
        if proxy is None: break
        api.update_status(proxy)
        print(proxy)
        time.sleep(900)
      except tweepy.TweepError as e:
        print("\033[36m" + str(e.api_code) + "\033[39m This address is already tweeted.")
      except KeyboardInterrupt:
        print("exit")
proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=["HTTP", "HTTPS", "Anonymous", "High"], limit=9999, timeout=8, attempts_tries=3, providers=['http://www.proxylists.net/', 'http://fineproxy.org/eng/', 'https://www.proxynova.com/proxy-server-list/', 'http://www.freeproxylists.net/', 'https://hidemy.name/en/proxy-list/', 'http://free-proxy.cz/en/'], countries = ['US', 'CN', 'BR', 'RU']),
		tweet(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)	


