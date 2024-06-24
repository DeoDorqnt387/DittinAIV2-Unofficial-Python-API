import requests
import os
import json

from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()

auth = os.getenv("AUTH")
chatListId = os.getenv("CHAT_LIST_ID")

class DittinAI:
    def __init__(self, url="https://beta.dittin.ai/"):
        self.url = url

    def fetch_page(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth}"
        }

        response = requests.get(self.url, headers=headers)
        if response.status_code ==200:
            print(response.status_code)
            return BeautifulSoup(response.text, "html.parser")
        else:
            print("Error", response.status_code)
            return None

    def chat(self,msg: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth}"
        }
        payload = {
            "action": "sendMessage",
            "data": {
                "chatListId": chatListId,
                "message": msg
            }
        }
        api_url = "https://beta.dittin.ai/api/chat"

        try:
            full_text = ""
            response = requests.post(api_url, headers=headers, json=payload)
            for line in response.iter_lines():
                if line:
                    try:
                        line_str = line.decode('utf-8')
                        if line_str.startswith("{\"text\":"):
                            data = json.loads(line_str)
                            full_text += data["text"]
                    except json.JSONDecodeError as e:
                        print("JSON decode error:", e)

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        return full_text
    
    def name(self, name: str):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth}"
        }
        payload = {
            "action": "updateUserInfo",
            "data": {
                "name": name,
            }
        }
        api_url = "https://beta.dittin.ai/api/user"
        requests.post(api_url, headers=headers, json=payload)
        print("Your Username Changed to: ", name)

    def bio(self, bio: str):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth}"
        }
        payload = {
            "action": "updateUserInfo",
            "data": {
                "bio": bio,
            }
        }
        api_url = "https://beta.dittin.ai/api/user"
        requests.post(api_url, headers=headers, json=payload)
        print("Your Bio Changed to: ", bio)