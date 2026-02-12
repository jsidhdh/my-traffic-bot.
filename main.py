import os
import requests

# --- Configuration ---
BLOG_ID = os.getenv('7821854519823506376')
API_KEY = os.getenv('
‏AIzaSyCfehr8CC_vNLVjahWuKGUEpzrrQ2Xfbcg')

def create_post(title, content):
    url = f"https://www.googleapis.com/shopping/content/v2.1" # Example URL
    # If using Blogger API:
    blogger_url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    
    payload = {
        "kind": "blogger#post",
        "title": title,
        "content": content
    }
    
    params = {'key': API_KEY}
    response = requests.post(blogger_url, json=payload, params=params)
    
    if response.status_code == 200:
        print("✅ Post Created Successfully!")
    else:
        print(f"❌ Error: {response.text}")

if __name__ == "__main__":
    # Test Content
    test_title = "My First Auto Post from Bot"
    test_content = "<h1>Hello!</h1><p>This post was created automatically by my bot.</p>"
    
    if BLOG_ID and API_KEY:
        create_post(test_title, test_content)
    else:
        print("❌ Missing BLOG_ID or API_KEY in Secrets!")
