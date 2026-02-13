import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def run_bot():
    # سحب بيانات المفتاح من جيت هاب
    info = json.loads(os.getenv('API_KEY'))
    bid = os.getenv('BLOG_ID')
    
    # تسجيل الدخول باستخدام حساب الخدمة
    sco = ['https://www.googleapis.com/auth/blogger']
    creds = service_account.Credentials.from_service_account_info(info, scopes=sco)
    service = build('blogger', 'v3', credentials=creds)

    # بيانات المقال للتجربة
    draft = {
        'kind': 'blogger#post',
        'title': 'تجربة النشر التلقائي 2026',
        'content': 'تم النشر بنجاح بواسطة TamBot بعد تحديث الصلاحيات! 🚀'
    }

    try:
        posts = service.posts().insert(blogId=bid, body=draft).execute()
        print(f"✅ تم النشر بنجاح! رابط المقال: {posts['url']}")
    except Exception as e:
        print(f"❌ لسه فيه مشكلة: {e}")

if __name__ == "__main__":
    run_bot()
