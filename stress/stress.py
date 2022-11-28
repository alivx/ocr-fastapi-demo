from locust import HttpUser, SequentialTaskSet, task, between
            
class User(HttpUser):    
    @task
    class SequenceOfTasks(SequentialTaskSet):
        wait_time = between(1, 5)
        @task
        def upload(self):
            headers = {
                'accept': 'application/json',
            }
            files = {
                'image': open('sample.png', 'rb'),
            }
            response = self.client.post('http://localhost:8000/upload', headers=headers, files=files)