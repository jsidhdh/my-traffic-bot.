import requests
from bs4 import BeautifulSoup

‎# --- إعداداتك الخاصة ---
BLOG_ID = "7821854519823506376"
API_KEY = "http://27304067439-hntv8ncnde7a90ot5d9d8bjka4f93a7l.apps.googleusercontent.com"
‎# رابط المنتج اللي أرسلته
PRODUCT_URL = "https://www.noon.com/uae-en/N46787424A/p/"

def scrape_and_post():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print("🔍 جاري فحص المنتج من نون...")
    try:
        response = requests.get(PRODUCT_URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

‎        # سحب اسم المنتج
        title = soup.find('h1').text.strip() if soup.find('h1') else "منتج مميز من نون"
        
‎        # سحب السعر (نون يغير الكود أحياناً، هذا كود تقريبي)
        price_tag = soup.find('div', {'class': 'priceNow'})
        price = price_tag.text.strip() if price_tag else "راجع الرابط للسعر"

        print(f"✅ تم سحب: {title}")

‎        # تجهيز محتوى المقال (HTML)
        post_content = f"""
        <h2>{title}</h2>
        <p>عرض حصري من نون!</p>
        <p><b>السعر الحالي:</b> {price}</p>
        <br>
        <a href="{PRODUCT_URL}" style="padding: 10px 20px; background-color: #feee00; color: #000; text-decoration: none; font-weight: bold; border-radius: 5px;">اضغط هنا للشراء مباشرة</a>
        <br><br>
        <p>تسوق الآن عبر رابطنا لدعم المحتوى.</p>
        """

‎        # إرسال المقال إلى بلوجر
        print("📤 جاري النشر في بلوجر...")
        publish_url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
        data = {
            "kind": "blogger#post",
            "title": title,
            "content": post_content
        }
        
        r = requests.post(f"{publish_url}?key={API_KEY}", json=data)
        
        if r.status_code == 200:
            print("🎉 مبروك! المنتج نزل في مدونتك تلقائياً.")
        else:
            print(f"❌ فشل النشر. خطأ: {r.text}")

    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    scrape_and_post()
