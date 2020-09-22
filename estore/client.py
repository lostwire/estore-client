import json

import estore.base

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

    async def add_event(self, event):
        headers = {
            'X-ES-Version': event.version }
        await self.__post(f"/{event.stream}/{event.name}", headers=event.headers, data=json.dumps(event.data))

    def __aiter__(self):
        return self.__iterator()

    async def __iterator(self):
        async with self.__http.ws_connect(f"{self.__url}/ws") as ws:
            async for msg in ws:
                yield msg.data
