import uuid
import json
import asyncio

import aiohttp

class Consume:
    def __init__(self, http):
        self.__http = http
    def __getitem__(self, item):
        return Stream(item)
    def __aiter__(self):
        return message_iterator(self.__http)

class Stream:
    def __init__(self, http):
        self.__http = http
    def __getitem__(self, item):
        return Stream(item)
    def __aiter__(self):
        return message_iterator(self.__http)


class Client:
    def __init__(self, url, http):
        self.__url = url
        self.__http = http

    async def __post(self, path, **kwargs):
        resp = await self.__http.post(f"{self.__url}{path}", **kwargs)
        return await resp.text()

    async def __get(self, path, **kwargs):
        resp = await self.__http.get(f"{self.__url}{path}", **kwargs)
        return await resp.text()

    async def add_event(self, stream, name, version, data):
        headers = {
            'X-ES-Version': version }
        await self.__post(f"/{stream}/{name}", headers=headers, data=json.dumps(data))

    def __aiter__(self):
        return message_iterator(self.__http)

async def message_iterator(http):
    async with http.ws_connect('http://172.21.0.1:8000/ws') as ws:
        async for msg in ws:
            yield msg.data


async def init():
    cookies = aiohttp.CookieJar(unsafe=True)
    async with aiohttp.ClientSession(cookie_jar=cookies) as session:
        cl = Client('http://172.21.0.1:8000', session)
        async for event in cl:
            print(event)


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
