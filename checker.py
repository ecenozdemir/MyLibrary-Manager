import pandas as pd

def check_book(new_isbn):
    try:
        df = pd.read_csv('books_db.csv')
        # ISBN numarasını kontrol et
        if str(new_isbn) in df['isbn'].astype(str).values:
            book_info = df[df['isbn'].astype(str) == str(new_isbn)]
            print(f"🚨 UYARI: Bu kitap zaten kütüphanende! Adı: {book_info['title'].values[0]}")
        else:
            print("✅ GÜVENLİ: Bu kitap kütüphanende yok, alabilirsin.")
    except FileNotFoundError:
        print("Kütüphane dosyası bulunamadı!")

# Kullanım:
sorgu = input("Kontrol etmek istediğin kitabın ISBN numarasını yaz: ")
check_book(sorgu)
