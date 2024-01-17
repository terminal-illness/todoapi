import requests

class TestApi:
    url = "http://127.0.0.1:8000/"
    
    def get_items(self):
        response = requests.get(self.url)
        return response

    def update_item(self, todoId: int):
        response = requests.get(self.url+f"update/{todoId}")
        return response

    def delete_item(self, todoId: int):
        response = requests.get(self.url+f"delete/{todoId}")
        return response
    
    def add_item(self, title: str ):
        response = requests.post(self.url+f"add", data={"title": title})
        return response

if __name__ == "__main__":
    test = TestApi()
    print(test.add_item("work"))
