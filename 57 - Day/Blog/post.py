import requests


class Post:
    def __init__(self):
        self.response = requests.get(url="https://api.npoint.io/e5592fcd4a56c826fe64")
        self.response.raise_for_status()
        self.all_post = self.response.json()

    def posts(self):
        return self.all_post
