import os
import requests

def start():
    b_id = os.getenv('7821854519823506376')
    a_key = os.getenv('
‏AIzaSyCfehr8CC_vNLVjahWuKGUEpzrrQ2Xfbcg')
    if not b_id or not a_key:
        print("Missing Keys")
        return
    
    url = f"https://www.googleapis.com/blogger/v3/blogs/{b_id}/posts/"
    data = {
        "kind": "blogger#post",
        "title": "Automated Post",
        "content": "Bot is working successfully!"
    }
    r = requests.post(url, params={'key': a_key}, json=data)
    print(r.status_code)
    print(r.text)

if __name__ == "__main__":
    start()
