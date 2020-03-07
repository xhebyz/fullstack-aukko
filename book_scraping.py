import requests
from bs4 import BeautifulSoup
import re
from config import db
from models import Book, Category



def remove_old_data():
    db.drop_all(bind=None)
    db.create_all()

def create_categories():
    url_scraping = "http://books.toscrape.com/index.html"
    result = requests.get(url_scraping)
    soup = BeautifulSoup(result.text, 'html.parser')

    categories_urls = [x.get('href') for x in soup.find_all("a", href=re.compile("catalogue/category/books"))]
    for url in categories_urls[1:]:
        url_data = soup.find("a", href=url)

        name = url_data.get_text()

        if name:
            name = name.strip()

        category = {
            "name": name
        }

        db.session.add(Category(
            name=name
        ))

        books = find_books(url, category)
        category["books"] = books

        print(category)
        db.session.commit()


def find_books(url_category, category):
    books = []
    url_scraping = "http://books.toscrape.com"
    url_catalogue = "http://books.toscrape.com/catalogue"

    result = requests.get(url_scraping + "/" + url_category)
    soup = BeautifulSoup(result.text, 'html.parser')

    main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_="product_pod")]
    for url in main_page_products_urls:
        url = url_catalogue + url.replace('../../..', '')

        result_book = requests.get(url)
        soup_book = BeautifulSoup(result_book.text, 'html.parser')

        names = soup_book.find("div", class_=re.compile("product_main")).h1.text
        prices = soup_book.find("p", class_="price_color").text
        nb_in_stock = re.sub("[^0-9]", "", soup_book.find("p", class_="instock availability").text)
        img_urls = url_scraping + (soup_book.find("img").get("src").replace("../..", ""))
        pd = soup_book.select_one('.product_page > p')
        product_description = pd.get_text(strip=True) if pd else ''
        upc = soup_book.select('.product_page table td')[0].get_text(strip=True)
        book = {
            'title': names,
            'prices': prices,
            'stock': (int(nb_in_stock) > 0),
            'thumbnail_url': img_urls,
            'price': prices,
            'product_description': product_description,
            'upc': upc,
            'category': category
        }

        category_data = Category.query.filter_by(name=category.get('name')).first()

        db.session.add(Book(
            category_id=category_data.id,
            title=book.get('title'),
            thumbnail_url=book.get('thumbnail_url'),
            stock=book.get('stock'),
            product_description=book.get('product_description'),
            price=book.get('price'),
            upc=book.get('upc')
        ))

        books.append(book)

    # NEXT PAGE

    next_class = soup.findAll("li", class_="next")

    if next_class:
        next_url = next_class[0].a.get('href')
        url_cat = url_category.split('/')
        url_cat[-1] = next_url
        next_cat_page = '/'.join(url_cat)
        page_books = find_books(next_cat_page, category)
        books = books + page_books

    return books


remove_old_data()
create_categories()