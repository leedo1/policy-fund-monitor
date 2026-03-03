import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.semas.or.kr/web/board/webBoardList.kmdc?bCd=1"

response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

today = datetime.now().strftime("%Y-%m-%d")

results = []

for row in soup.select("table tbody tr")[:5]:
    title_tag = row.select_one("td:nth-child(2) a")
    if title_tag:
        title = title_tag.text.strip()
        results.append(title)

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"[{today} 정책자금 신규 공고 요약]\n\n")
    for i, item in enumerate(results, 1):
        f.write(f"{i}. {item}\n")

print("완료")
