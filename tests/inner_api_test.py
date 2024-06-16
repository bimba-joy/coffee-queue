from locust import HttpUser, task


class MyWorker(HttpUser):

    @task
    def load_test_start(self):
        self.client.get("/start/")

    @task
    def load_test_finish(self):
        self.client.post("/finish/", json={"order_id": 1})
