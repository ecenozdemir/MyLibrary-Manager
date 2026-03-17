CREATE TABLE books (
    isbn TEXT PRIMARY KEY,       -- Her kitabın arkasındaki benzersiz barkod numarası
    book_name TEXT NOT NULL,     -- Kitap Adı
    author TEXT,                 -- Yazar
    category TEXT,               -- Tür (Roman, Tarih, Yazılım vb.)
    purchase_date DATE,          -- Alınan tarih
    status TEXT DEFAULT 'Unread' -- Durum (Okundu, Okunmadı, Okunuyor)
);
