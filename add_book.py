import requests
import pandas as pd
import os

def get_book_details(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                book_info = data['items'][0]['volumeInfo']
                title = book_info.get('title', 'Bilinmiyor')
                authors = ", ".join(book_info.get('authors', ['Bilinmiyor']))
                return title, authors
    except:
        pass
    return None, None

def add_to_library():
    isbn = input("📚 Eklemek istediğin kitabın ISBN numarasını gir: ")
    
    # 1. Mükerrer Kontrolü
    if os.path.exists('books_db.csv'):
        df = pd.read_csv('books_db.csv')
        if str(isbn) in df['isbn'].astype(str).values:
            book_info = df[df['isbn'].astype(str) == str(isbn)]
            print(f"🚨 UYARI: Bu kitap zaten kütüphanende kayıtlı! ({book_info['title'].values[0]})")
            return

    # 2. Otomatik Bilgi Getirme
    title, author = get_book_details(isbn)
    
    if title:
        print(f"\n🔍 Bulunan Bilgi:")
        print(f"Kitap: {title}")
        print(f"Yazar: {author}")
        onay = input("\nBu bilgiler doğru mu? (E/H): ").upper()
        
        if onay != 'E':
            print("\n✍️ O zaman bilgileri manuel girelim:")
            title = input("Kitabın tam adını yaz: ")
            author = input("Yazarın adını yaz: ")
    else:
        print("\n❌ İnternette bu ISBN ile ilgili bilgi bulunamadı.")
        title = input("✍️ Kitabın adını manuel gir: ")
        author = input("✍️ Yazarın adını manuel gir: ")

    # 3. Kaydetme
    status = input("Okuma durumu (Okundu/Okunmadı/Okunuyor): ")
    
    new_data = pd.DataFrame([[isbn, title, author, status]], 
                            columns=['isbn', 'title', 'author', 'status'])
    
    file_exists = os.path.isfile('books_db.csv')
    new_data.to_csv('books_db.csv', mode='a', header=not file_exists, index=False)
    
    print(f"\n✅ BAŞARILI: '{title}' envanterine eklendi!")

if __name__ == "__main__":
    add_to_library()
