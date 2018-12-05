from django.core.management.base import BaseCommand, CommandError
from MySite.maintitle.models import Books, Authors
import bs4
import requests


# return html page
def download_page(page):
    url = 'https://mybook.ru/catalog/fentezi/fentezi-pro-drakonov/books/?page=%d' % page
    request = requests.get(url)
    if request.status_code == 404:
        return None
    return request.text


# return author, book_name, description
def download_book_info(href):
    url = 'https://mybook.ru/%s' % href
    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.text, 'html.parser')
    author = soup.find('div', {'class': 'book-page-author'}).find('a').text.strip()
    book_name = soup.find('div', {'class': 'book-page-book-name'}).text.strip()
    description = soup.find('div', {'class': "definition-section"}).find('p').text
    return author, book_name, description


# return author, description
def dowlnoad_author_info(href):
    url = 'https://mybook.ru/%s' % href
    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.text, 'html.parser')
    author = soup.find('h1', {'class': 'author-page-name'}).text.strip()
    try:
        description = soup.find('div', {'class': 'text-expander-inner js-comment-content-expander-text'}).text.strip()
    except AttributeError:
        description = None
    return author, description


def main():
    page = 1
    while True:
        response = download_page(page)
        if response is None:
            break
        soup = bs4.BeautifulSoup(response, 'html.parser')
        items_collections = soup.find('div', {"class": "items-collection"})
        item = items_collections.find_all('li', {"class": ["item", "item -feature"]})
        for book in item:
            book_href = book.find('div', {"class": 'book-name'}).find('a').get('href')
            author_href = book.find('div', {"class": 'book-author'}).find('a').get('href')
            # нужно добавить проверку наличия этой книги и автора
            Books.objects.create(author='%s', book_name='%s', description='%s' % download_book_info(book_href))
            Authors.objects.create(author='%s', description='%s' % dowlnoad_author_info(author_href))
        page += 1


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
