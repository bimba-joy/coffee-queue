import aiohttp
from fastapi import FastAPI
from queue import Queue

from domain import OrderRequest

inner_app = FastAPI()
order_queue = Queue()
orders = {}


@inner_app.get("/start/")
async def start_order():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:9999/start_working/') as response:
            return await response.json()


@inner_app.post("/finish/")
async def finish_order(order: OrderRequest):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:9999/finish_working/', json={'order_id': order.order_id}) as response:
            return await response.json()


@inner_app.get("/ping/")
async def ping():
    return {"details": "OK", "service": "inner"}
