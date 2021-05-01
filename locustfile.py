from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
        wait_time = between(4, 6)
        @task
        def index(self):
                # print("executing my task")
                # self.client.get("/")
                self.client.get("/predict?url=https://yelpmodel0907.s3.amazonaws.com/Images/images/drink.jpeg")
