import sqlite3

def check_duplicate(isbn_to_check):
    # Bu fonksiyon ilerde gerçek veritabanına bağlanacak
    # Şimdilik mantığı kuruyoruz
    library_data = [
        {"isbn": "9786053755356", "name": "Cesur Yeni Dünya"},
        {"isbn": "9789750719387", "name": "1984"}
    ]
    
    for book in library_data:
        if book['isbn'] == isbn_to_check:
            return f"❌ DUR! '{book['name']}' zaten kütüphanende var."
    
    return "✅ BU KİTAP SİSTEMDE YOK: Güvenle alabilirsin!"

# Test edelim
test_isbn = "9789750719387"
print(check_duplicate(test_isbn))
