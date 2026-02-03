import feedparser
import openpyxl
import os
import urllib.parse  
from datetime import datetime

def update_excel_news(keyword):
    # キーワードをURL用に変換
    encoded_keyword = urllib.parse.quote(keyword)
    
    # 変換したキーワードをURLに組み込む
    rss_url = f"https://news.google.com/rss/search?q={encoded_keyword}&hl=ja&gl=JP&ceid=JP:ja"
    
    feed = feedparser.parse(rss_url)
    
    # --- この先は前のコードと同じ ---
    # パスが正しいか確認
    EXCEL_PATH = r"自身の作成したファイルパス" 
    
    if not os.path.exists(EXCEL_PATH):
        print("ファイルが見つかりません。")
        return

    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active

    for entry in feed.entries[:10]:
        sheet.append([entry.title, entry.link, entry.published])

    wb.save(EXCEL_PATH)
    print(f"「{keyword}」のニュースを保存しました！")

# 実行
update_excel_news("ニュース")