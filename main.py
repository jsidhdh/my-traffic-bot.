import requests

links = [
    "https://mashlexpress.blogspot.com/2026/02/mas11.html",
    "https://www.noon.com/saudi-ar/?referrer=7821854519823506376&utm_source=MAS11"
]

def run():
    # إنشاء جلسة (Session) تحاكي المتصفح بشكل أدق
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "ar-SA,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.google.com/"
    })

    print("🚀 Starting Smart Visits...")
    for url in links:
        try:
            # نمر عبر جوجل أولاً كأننا قادمون من بحث
            r = session.get(url, timeout=20)
            if r.status_code == 200:
                print(f"✅ SUCCESS: {url}")
            else:
                print(f"⚠️ BLOCKED: {url} (Status: {r.status_code})")
        except:
            print(f"❌ FAILED: {url}")

if __name__ == "__main__":
    run()
