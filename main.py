import csv
import requests
from bs4 import BeautifulSoup

# 输入 CSV 文件路径
input_file = "/content/web.csv"
output_file = "/content/extracted_urls.csv"

# 从 web.csv 中读取数据
urls = []
with open(input_file, "r") as input_csv:
    reader = csv.DictReader(input_csv)
    column_names = reader.fieldnames
    for row in reader:
        url_data = {
            column_names[0]: row[column_names[0]],
            column_names[1]: row[column_names[1]]
        }
        urls.append(url_data)

# 从每个 URL 中提取标题、时间和正文
for url_data in urls:
    try:
        response = requests.get(url_data[column_names[1]])
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.find("title")
        url_data["title"] = title.text.strip() if title else "No Title"

        published_date = soup.find("publishtime")
        url_data["published_date"] = published_date.text.strip() if published_date else "No Date"

        content_paragraphs = soup.find_all("p")
        url_data["content"] = "\n".join([p.text.strip() for p in content_paragraphs]) if content_paragraphs else "No Content"
    except Exception as e:
        print(f"Error processing URL: {url_data[column_names[1]]} - {e}")
        url_data["title"] = "Error"
        url_data["published_date"] = "Error"
        url_data["content"] = "Error"

# 将数据写入 extracted_urls.csv
with open(output_file, "w", newline="", encoding="utf-8") as output_csv:
    fieldnames = column_names + ["title", "published_date", "content"]
    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    writer.writeheader()

    for url_data in urls:
        writer.writerow(url_data)

print("Data has been extracted and saved to /content/extracted_urls.csv.")
