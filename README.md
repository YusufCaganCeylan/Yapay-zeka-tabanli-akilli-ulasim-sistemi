# Yapay-zeka-tabanli-akilli-ulasim-sistemi

Bu proje, trafik kazalarını gerçek zamanlı olarak tespit ederek, olayın şiddetine göre görsel ve işitsel uyarılar üreten bir sistemdir. Sistem, Raspberry Pi 5 üzerinde çalışmakta ve YOLOv8 modeli kullanmaktadır.

## Özellikler
- **Anlık Kaza Tespiti**: YOLOv8 modeli sayesinde kazalar anında tespit edilir.
- **Şiddet Sınıflandırması**: Kazalar "ağır" (severe) ve "orta" (moderate) olarak sınıflandırılır.
- **Donanım Uyarı Mekanizması**: LED'ler ve buzzer'lar ile görsel ve işitsel uyarı sağlar.
- **Gerçek Zamanlı Görselleştirme**: Tespit edilen kazalar anlık olarak ekranda gösterilir.

## Gerekli Donanımlar
- Raspberry Pi 5
- Raspberry Pi Kamera Modülü
- LED (2 adet)
- Buzzer (2 adet)
- GPIO bağlantı kabloları

## Kurulum
1. **Gerekli Paketleri Kurun**:
   ```bash
   pip install -r requirements.txt
