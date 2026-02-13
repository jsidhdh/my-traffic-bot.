import os, requests

def publish_all():
    bid = os.getenv('7821854519823506376')
    key = os.getenv('
‏AIzaSyCfehr8CC_vNLVjahWuKGUEpzrrQ2Xfbcg
')
    
    # قائمة المنتجات اللي أرسلتها يا مشعل
    products = [
        {
            "title": "سماعة هواوي FreeBuds SE 2 - بطارية 40 ساعة",
            "img": "https://f.nooncdn.com/p/v1691402284/N53401569A_1.jpg",
            "link": "https://www.noon.com/saudi-ar/freebuds-se-2-in-ear-earphones-true-wireless-earbuds-40-hour-battery-life-3-hours-of-music-playback-on-a-10-minute-charge-compact-and-comfortable-black/N70075990V/p/?o=a0a4351361abefbb&shareId=71d94f61-d7c7-40e1-aa8b-ea0d9040c0ff"
        },
        {
            "title": "سماعة الألعاب SoulBytes S22 Pro - إضاءة LED",
            "img": "https://f.nooncdn.com/p/v1714545362/N70255036V_1.jpg",
            "link": "https://www.noon.com/saudi-ar/soulbytes-s22-pro-gaming-wired-over-the-ear-headsets-with-mic-led-for-ps4-ps5-xbox-one-xbox-series-nintendo-switch-and-pc/N70255036V/p/?o=b423010c848ab54f&shareId=987fe2eb-a9dd-4b6f-ba66-8f9c82273c10"
        },
        {
            "title": "iPhone 17 Pro Max - اللون البرتقالي الكوني الجديد",
            "img": "https://f.nooncdn.com/p/v1725961628/N70211545V_1.jpg",
            "link": "https://www.noon.com/saudi-ar/iphone-17-pro-max-256-gb-cosmic-orange-5g-esim-only-with-facetime-middle-east-version/N70211545V/p/?o=bd982e95c96f493a&shareId=9ed9fba6-4946-4dc0-9e76-c218ada650a7"
        }
    ]

    for p in products:
        content = f"""
        <div dir="rtl" style="text-align: right; font-family: sans-serif; border: 1px solid #ddd; padding: 20px; border-radius: 15px; margin-bottom: 20px;">
            <h2 style="color: #333;">{p['title']}</h2>
            <center><img src="{p['img']}" style="width: 100%; max-width: 300px; border-radius: 10px;" /></center>
            <p>منتج مميز متوفر الآن على نون بأفضل الأسعار.</p>
            <center>
                <a href="{p['link']}" style="background-color: #feee00; color: #000; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 8px; display: inline-block;">
                    اشتري الآن من نون 🛒
                </a>
            </center>
        </div>
        """
        
        url = f"https://www.googleapis.com/blogger/v3/blogs/{bid}/posts/"
        payload = {"kind": "blogger#post", "title": p['title'], "content": content}
        r = requests.post(url, params={'key': key}, json=payload)
        
        if r.status_code == 200:
            print(f"✅ تم نشر: {p['title']}")
        else:
            print(f"❌ خطأ في {p['title']}: {r.text}")

if __name__ == "__main__":
    publish_all()
