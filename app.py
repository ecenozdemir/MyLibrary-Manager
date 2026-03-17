import streamlit as st
import pandas as pd
import requests

st.title("📚 Ece'nin Kişisel Kütüphanesi")
st.subheader("Yeni Kitap Ekle & Mükerrer Kontrolü")

isbn = st.text_input("Kitabın ISBN Numarasını Girin veya Okutun:")

if isbn:
    # Google Books'tan sorgula
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    res = requests.get(url).json()
    
    if 'items' in res:
        book = res['items'][0]['volumeInfo']
        title = book.get('title')
        author = ", ".join(book.get('authors', []))
        
        st.write(f"### 🔍 Bulunan Kitap: {title}")
        st.write(f"**Yazar:** {author}")
        
        if st.button("Kitaplığıma Ekle"):
            st.success(f"✅ {title} başarıyla eklendi!")
            # Burada ilerde CSV veya SQL veritabanına kayıt yapacağız
    else:
        st.error("Kitap bulunamadı, lütfen manuel girin.")
