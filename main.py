import requests

# هذي روابطك اللي تبيها تزيد
links = [
    "https://mashlexpress.blogspot.com/2026/02/mas11.html",
    "https://www.noon.com/saudi-ar/?referrer=7821854519823506376&utm_source=MAS11"
]

def run_visit():
    print("🚀 Starting visits...")
    for url in links:
        try:
            r = requests.get(url, timeout=10)
            print(f"✅ Visited: {url} | Status: {r.status_code}")
        except:
            print(f"❌ Failed: {url}")

if __name__ == "__main__":
    run_visit()
