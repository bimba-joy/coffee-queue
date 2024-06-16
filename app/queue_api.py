import random
import time
from queue import Queue
from threading import Thread

from fastapi import FastAPI, Request, HTTPException

from domain import Order, OrderRequest

queue_app = FastAPI()
order_queue = Queue()
order_counter = 0
orders = {}


@queue_app.post('/new_order/')
async def new_order(request: Request):
    global order_counter
    order_counter += 1
    order_id = order_counter
    order = Order(id=order_id, client_ip=request.client.host)
    orders[order_id] = order
    order_queue.put(order_id)
    return {'message': 'Order created', 'order_id': order_id}


@queue_app.get('/status/{order_id}')
async def order_status(order_id: int):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"order_id": order_id, "status": orders[order_id].status}


@queue_app.get('/start_working/')
async def start_working():
    if order_queue.empty():
        raise HTTPException(status_code=404, detail="No order to process")
    order_id = order_queue.get()
    orders[order_id].status = "in-progress"
    Thread(target=process_order, args=(order_id,)).start()
    return {"message": "Order started", "order_id": order_id}


def process_order(order_id: int):
    time_to_brew = random.randint(30, 60)
    time.sleep(time_to_brew)
    orders[order_id].status = "finished"


@queue_app.post('/finish_working/')
async def finish_working(order: OrderRequest):
    if order.order_id not in orders or orders[order.order_id].status != 'in-progress':
        raise HTTPException(status_code=404, detail='Order not found or not in-progress')
    orders[order.order_id].status = 'finished'
    return {'message': 'Order is done', 'order_id': order.order_id}


@queue_app.get("/ping/")
async def ping():
    return {"details": "OK", "service": "queue"}
