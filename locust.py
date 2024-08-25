from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(5, 15)  # Time between requests in seconds

    @task
    def my_task(self):
        self.client.get("/my_endpoint")
