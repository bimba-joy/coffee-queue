from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_test_order(self):
        self.client.post("/order/")
        
    @task
    def load_test_order_status(self):
        self.client.get("/order/1")
