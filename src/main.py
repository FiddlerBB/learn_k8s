import requests
from selectolax.parser import HTMLParser
from typing import List, Dict
import csv, time

def get_site(url: str):
    """
    This function takes a URL as input and returns the HTML content of the website.
    """
    res = requests.get(url)
    data = res.content
    return data 

def parse_(html: str):
    """
    This function takes the HTML content of a website and returns a list of links
    found on the page.
    """
    html = HTMLParser(html)

    books = html.css('article')
    records = []
    for book in books:
        title  = book.css_first('h3 > a').attributes.get('title')
        rating = book.css_first('p.star-rating').attributes.get('class').split(' ')[1]
        price = book.css_first('div > p.price_color').text().strip('£')
        avail = book.css_first('p.instock').text().strip()
        
        records.append(
            {
            'title': title.replace('"', ''),
            'rating': rating,
            'price': float(price),
            'in-stock': avail
            }
        )
    for data in records:
        print(data)
    return records

def save_file(data: List[Dict]):
    header = data[0].keys()
    with open('./out/books.csv', 'w') as f:
        dw = csv.DictWriter(f, header)
        dw.writeheader()
        dw.writerows(data)

def loop_to_get_log(num):
    for i in range(num):
        print(f'Counting: {i}')
        time.sleep(1)


def main():
    url = 'https://books.toscrape.com/'
    data = get_site(url)
    records = parse_(data)
    save_file(records)
    loop_to_get_log(300)

if __name__ == '__main__':
    main()
    