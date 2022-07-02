import tweepy
import asyncio
import json
import requests
import os
from threading import Timer

from utils.requests import better_object, deserialize, fetch, gimmick

endpoint = ["fgo", "genshin_impact", "azur_lane", "waifu", "arknights",
           "fire_emblem", "gfl", "hololive", "kancolle", "sex", "gelbooru", "r34", "safebooru"]

animesex = ["ass", "bdsm", "cum", "creampie", "manga", "femdom", "hentai", "incest",
            "masturbation", "public", "ero", "orgy", "elves", "yuri", "pantsu",
            "glasses", "cuckold", "blowjob", "boobjob", "foot", "thighs", 
            "vagina", "ahegao", "uniform"]


def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()


def hello():
    async def main() -> str:
        req = await fetch(f"https://scathach.redsplit.org/v5/{endpoint[0]}/")
        data = json.loads(better_object(req))
        return data
        
    try:
        raw = asyncio.run(main())
        img_data = requests.get(raw['image']).content
        with open('content.jpg', 'wb') as handler:
            handler.write(img_data)

        auth = tweepy.OAuthHandler("abc")
        auth.set_access_token("badada", "xixixi")

        api = tweepy.API(auth)

        filename = 'content.jpg'
        status = f"{raw['data']['character']}"
        status = status.replace("%27", "'")

        if os.path.getsize(filename) > 3000000:
            api.update_status("413 Payload Too Large")
            print("413 Payload Too Large")
            os.remove(filename)

        else:
            api.update_status_with_media(f"{status}\n{gimmick()}", filename)
            print("Tweeted")
            os.remove(filename)

    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    setInterval(60.0, hello)
