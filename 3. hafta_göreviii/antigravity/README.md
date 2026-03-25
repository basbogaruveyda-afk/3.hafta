# Veri Seti Kurgusu: Mobil Güç ve Termal Analiz

Bu veri seti, yeni nesil bir akıllı telefonun stres testi altındaki batarya performansını temsil etmektedir. Mühendislik standartlarında bir cihazın verimliliğini ölçmek amacıyla oluşturulan bu sentetik veriler, donanımın ısıl değerleri ile enerji tüketim hızı arasındaki ilişkiyi yansıtır. Veri setinde yer alan iki temel değişken şunlardır:

- **Ekran Süresi (Screen-On Time):** Cihazın %100 doluluktan kapanana kadar sunduğu aktif kullanım süresini temsil eder. Birimi saat (h) olan bu değişken, ortalama $7 \pm 1$ saatlik bir dağılım sergileyerek yazılım optimizasyonunun başarısını gösterir.
- **Batarya Sıcaklığı (Battery Temperature):** Kullanım esnasında batarya hücrelerinde ölçülen anlık veya ortalama termal değerdir. Birimi Santigrat Derece (°C) olup, ortalama $35 \pm 3$ °C değerindedir.

Bu iki değişkenin birlikte analizi, "hata payı" (margin of error) ve "performans standartları" (benchmarks) gibi kritik mühendislik kavramlarını somutlaştırır. Örneğin; sıcaklığın standart sapmanın üzerine çıktığı durumlarda, ekran süresindeki düşüşün (termal kısıtlama/throttling) nasıl tetiklendiği bu veri seti üzerinden gözlemlenebilir.
