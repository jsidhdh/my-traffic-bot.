import requests

links = [
    "https://mashlexpress.blogspot.com/2026/02/mas11.html",
    "https://www.noon.com/saudi-ar/?referrer=7821854519823506376&utm_source=MAS11"
]

# هذي الهيدرز تخلي المواقع تحسبنا داخلين من جوجل كروم حقيقي
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def run_visit():
    print("🚀 Starting Professional Visits...")
    for url in links:
        try:
            # هنا أضفنا الـ headers عشان نتخطى الحماية
            r = requests.get(url, headers=headers, timeout=15)
            print(f"✅ SUCCESS: {url} | Status: {r.status_code}")
        except Exception as e:
            print(f"❌ ERROR: {url}")

if __name__ == "__main__":
    run_visit()
