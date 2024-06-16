import uvicorn
from multiprocessing import Process
from inner_api import inner_app
from outer_api import outer_app
from queue_api import queue_app


def start_outer_api():
    uvicorn.run(outer_app, host="0.0.0.0")


def start_inner_api():
    uvicorn.run(inner_app, host="0.0.0.0", port=8001)


def start_queue_api():
    uvicorn.run(queue_app, host="0.0.0.0", port=9999)


if __name__ == "__main__":
    outer_process = Process(target=start_outer_api)
    inner_process = Process(target=start_inner_api)
    queue_process = Process(target=start_queue_api)

    outer_process.start()
    inner_process.start()
    queue_process.start()

    outer_process.join()
    inner_process.join()
    queue_process.join()
