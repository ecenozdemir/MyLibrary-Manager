import streamlit as st
import pandas as pd
import requests
import os

# Sayfa Ayarları
st.set_page_config(page_title="Ece'nin Kitaplığı", page_icon="📚")
st.title("📚 Ece'nin Kişisel Kütüphanesi")

# Dosya yolu (GitHub'daki veritabanımız)
DB_FILE = 'books_db.csv'

# Veritabanını Yükle
if os.path.exists(DB_FILE):
    df = pd.read_csv(DB_FILE)
else:
    df = pd.DataFrame(columns=['isbn', 'title', 'author', 'status'])

# --- YENİ KİTAP EKLEME BÖLÜMÜ ---
st.subheader("Yeni Kitap Ekle")
isbn_input = st.text_input("Kitabın ISBN Numarasını Girin:")

if isbn_input:
    # 1. Mükerrer Kontrolü
    if isbn_input in df['isbn'].astype(str).values:
        existing_book = df[df['isbn'].astype(str) == isbn_input].iloc[0]
        st.warning(f"🚨 Bu kitap zaten kütüphanende: **{existing_book['title']}**")
    else:
        # 2. İnternetten Bilgi Getir
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn_input}"
        try:
            res = requests.get(url).json()
            found_title = res['items'][0]['volumeInfo'].get('title', "") if 'items' in res else ""
            found_author = ", ".join(res['items'][0]['volumeInfo'].get('authors', [])) if 'items' in res else ""
        except:
            found_title, found_author = "", ""

        # 3. Form Alanı (Onay ve Düzeltme)
        with st.form("add_form"):
            st.info("Bilgileri kontrol et, gerekirse düzelt:")
            final_title = st.text_input("Kitap Adı", value=found_title)
            final_author = st.text_input("Yazar", value=found_author)
            final_status = st.selectbox("Durum", ["Okunmadı", "Okunuyor", "Okundu"])
            
            submit = st.form_submit_button("Kitaplığıma Kaydet")
            
            if submit:
                if final_title and final_author:
                    new_row = {'isbn': isbn_input, 'title': final_title, 'author': final_author, 'status': final_status}
                    # Burada şimdilik ekrana yazdırıyoruz, Streamlit Cloud bağlandığında dosyaya yazacak
                    st.success(f"✅ '{final_title}' başarıyla listene eklendi!")
                else:
                    st.error("Lütfen kitap adı ve yazar bilgilerini doldur.")

# --- LİSTE GÖRÜNTÜLEME BÖLÜMÜ ---
st.divider()
st.subheader("📖 Mevcut Kitaplığım")
st.dataframe(df, use_container_width=True)
