import tweepy
import asyncio
import json
import requests
import os
from threading import Timer

from utils.requests import better_object, deserialize, fetch, hack

enpoint = ["fgo", "genshin_impact", "azur_lane", "waifu", "arknights", "fire_emblem", "gfl", "hololive"]

def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()

def hello():
    async def main() -> str:
        req = await fetch("https://scathach.redsplit.org/v5/fgo/")
        data = json.loads(better_object(req))
        return data
    try:
        raw = asyncio.run(main())
        img_data = requests.get(raw['image']).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)

        auth = tweepy.OAuthHandler("abc")
        auth.set_access_token("badada", "xixixi")

        api = tweepy.API(auth)

        filename = 'image_name.jpg'
        status = f"{raw['data']['character']}"
        status = status.replace("%27", "'")

        if os.path.getsize(filename) > 3000000:
            api.update_status("413 Payload Too Large")
            print("413 Payload Too Large")
            os.remove(filename)
        
        else:
            api.update_status_with_media(f"{status}\n{hack()}", filename)
            print("Tweeted")
            os.remove(filename)

    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    setInterval(120.0, hello) 
    