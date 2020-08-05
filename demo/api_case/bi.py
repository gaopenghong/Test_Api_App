import bs4
import requests

# 爬取电影天堂的所有电影名
global page_numbers
try:
    page_numbers = 581  # 做成持久化的

    f = "D:\PythonWorkSpace\data\movies"
    while page_numbers < 1000:
        url = "http://ldytt.com/List/1-pg-%s.html" % page_numbers
        print(url)
        r = requests.get(url=url)
        r.raise_for_status()
        print(r)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        result = soup.select("img", class_="lazy")
        print(result)

        for i in result:
            print(i['alt'])
            movies_name = i['alt']
            with open(f, "a+") as file:
                file.write(movies_name + "\n")

        page_numbers = page_numbers + 1
        print(page_numbers)
except  UnicodeEncodeError:
    page_numbers = page_numbers + 2
    print("更新page_number")
