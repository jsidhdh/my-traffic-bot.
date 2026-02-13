import os, requests

def publish():
    bid = os.getenv('7821854519823506376')
    key = os.getenv('
‏AIzaSyCfehr8CC_vNLVjahWuKGUEpzrrQ2Xfbcg')
    
    # Data List
    prods = [
        {"t": "Huawei FreeBuds SE 2", "i": "https://f.nooncdn.com/p/v1691402284/N53401569A_1.jpg", "l": "https://www.noon.com/saudi-ar/freebuds-se-2-in-ear-earphones-true-wireless-earbuds-40-hour-battery-life-3-hours-of-music-playback-on-a-10-minute-charge-compact-and-comfortable-black/N70075990V/p/?o=a0a4351361abefbb&shareId=71d94f61-d7c7-40e1-aa8b-ea0d9040c0ff"},
        {"t": "SoulBytes S22 Pro Gaming", "i": "https://f.nooncdn.com/p/v1714545362/N70255036V_1.jpg", "l": "https://www.noon.com/saudi-ar/soulbytes-s22-pro-gaming-wired-over-the-ear-headsets-with-mic-led-for-ps4-ps5-xbox-one-xbox-series-nintendo-switch-and-pc/N70255036V/p/?o=b423010c848ab54f&shareId=987fe2eb-a9dd-4b6f-ba66-8f9c82273c10"},
        {"t": "iPhone 17 Pro Max Cosmic Orange", "i": "https://f.nooncdn.com/p/v1725961628/N70211545V_1.jpg", "l": "https://www.noon.com/saudi-ar/iphone-17-pro-max-256-gb-cosmic-orange-5g-esim-only-with-facetime-middle-east-version/N70211545V/p/?o=bd982e95c96f493a&shareId=9ed9fba6-4946-4dc0-9e76-c218ada650a7"}
    ]

    for p in prods:
        title = p["t"]
        link = p["l"]
        img = p["i"]
        content = f"<div dir='rtl'><h2>{title}</h2><img src='{img}' style='width:300px'/><br><a href='{link}'>Buy Now - اطلب الآن</a></div>"
        
        url = f"https://www.googleapis.com/blogger/v3/blogs/{bid}/posts/"
        payload = {"kind": "blogger#post", "title": title, "content": content}
        r = requests.post(url, params={'key': key}, json=payload)
        print(f"Post {title}: {r.status_code}")

if __name__ == "__main__":
    publish()
