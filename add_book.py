import requests
import pandas as pd
import os

def get_book_details(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            book_info = data['items'][0]['volumeInfo']
            title = book_info.get('title', 'Bilinmiyor')
            authors = ", ".join(book_info.get('authors', ['Bilinmiyor']))
            return title, authors
    return None, None

def add_to_library(isbn):
    # Önce mükerrer kontrolü yapalım
    if os.path.exists('books_db.csv'):
        df = pd.read_csv('books_db.csv')
        if str(isbn) in df['isbn'].astype(str).values:
            print(f"🚨 UYARI: Bu kitap zaten kayıtlı!")
            return

    # İnternetten bilgileri çek
    title, author = get_book_details(isbn)
    if title:
        new_data = pd.DataFrame([[isbn, title, author, 'Okunmadı']], 
                                columns=['isbn', 'title', 'author', 'status'])
        new_data.to_csv('books_db.csv', mode='a', header=not os.path.exists('books_db.csv'), index=False)
        print(f"✅ EKLENDİ: {title} - {author}")
    else:
        print("❌ HATA: Kitap bilgileri bulunamadı.")

# Kullanım
isbn_input = input("Eklemek istediğin kitabın ISBN numarasını gir: ")
add_to_library(isbn_input)
