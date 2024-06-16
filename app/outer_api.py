import aiohttp
from fastapi import FastAPI, Request

from ddos_protection import ddos_protection

outer_app = FastAPI()


@outer_app.post("/order/")
async def create_order(request: Request):
    ddos_protection(request)
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:9999/new_order') as response:
            return await response.json()


@outer_app.get("/order/{order_id}")
async def check_order(order_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:9999/status/{order_id}') as response:
            return await response.json()
