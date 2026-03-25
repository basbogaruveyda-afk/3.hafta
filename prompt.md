# Yapay Zeka ile Veri Üretimi ve Görselleştirme Örneği

**Öğrenci:** antigravity klasörü içinde çalışacak şekilde bir Python scripti oluştur. Şunları yapsın:
- "3.hafta" adında bir klasör oluştur.
- Bu klasörün içine "batarya_data.py" adında bir Python dosyası yazsın.
- Bu Python dosyası çalıştırıldığında:
  - 500 satırlık bir veri seti üretsin.
  - Sütunlar: ID, Ekran_Suresi (ortalama 7 saat, standart sapma 1 olacak şekilde normal dağılım), Batarya_Sicakligi (ortalama 35°C, standart sapma 3 olacak şekilde normal dağılım)
  - Veriler rastgele değil, numpy ile normal dağılımdan üretilsin.
  - Değerler mantıklı aralıklarda sınırlandırılsın (örneğin ekran süresi negatif olmasın).
- Oluşturulan veri setini "3.hafta/data.csv" olarak kaydetsin.
- Eğer "3.hafta" klasörü yoksa otomatik oluştursun.
- Kod en sonda otomatik çalışsın (yani veri seti direkt oluşsun).
Kod tamamen çalışır ve temiz olsun.

**Yapay Zeka (AI):** Merhaba! İstediğin veri üretim sistemini hazırlıyorum. `antigravity/setup_data.py` adlı bir kurulum dosyası oluşturdum. Bu dosya çalıştırıldığında gerekli klasörü (`3.hafta`) oluşturur, veri üretim kodunu (`batarya_data.py`) yazar ve ardından bu kodu otomatik olarak çalıştırarak CSV dosyasını üretir.

`setup_data.py` içeriği:
```python
import os
import subprocess
import sys

# Dosya yolları
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEEK_DIR = os.path.join(BASE_DIR, "3.hafta")
SCRIPT_NAME = "batarya_data.py"
SCRIPT_PATH = os.path.join(WEEK_DIR, SCRIPT_NAME)

# 1. Klasör Oluşturma
if not os.path.exists(WEEK_DIR):
    os.makedirs(WEEK_DIR)

# 2. Veri Üretim Scriptini Yazma
python_code = """
import numpy as np
import pandas as pd
import os

n_rows = 500
mean_screen_time = 7
std_screen_time = 1
mean_temp = 35
std_temp = 3

screen_time = np.random.normal(mean_screen_time, std_screen_time, n_rows)
battery_temp = np.random.normal(mean_temp, std_temp, n_rows)

screen_time = np.clip(screen_time, 0, 24)
battery_temp = np.clip(battery_temp, 0, 100)

df = pd.DataFrame({
    'ID': np.arange(1, n_rows + 1),
    'Ekran_Suresi': np.round(screen_time, 2),
    'Batarya_Sicakligi': np.round(battery_temp, 2)
})

csv_path = os.path.join(os.path.dirname(__file__), 'data.csv')
df.to_csv(csv_path, index=False)
print(f"Veri seti başarıyla oluşturuldu: {csv_path}")
"""

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(python_code.strip())

# 3. Otomatik Çalıştırma
subprocess.run([sys.executable, SCRIPT_PATH], check=True)
```

---

**Öğrenci:** csv dosyasını da verir misin

**Yapay Zeka (AI):** Tabii, oluşturulan veri setinin ilk birkaç satırı şu şekilde (dosya yolu `3.hafta/data.csv`):

```csv
ID,Ekran_Suresi,Batarya_Sicakligi
1,6.92,33.31
2,6.25,36.75
3,7.38,36.94
4,6.26,37.05
5,7.19,35.89
...
```

---

**Öğrenci:** görselleştirmeyi de yapar mısın

**Yapay Zeka (AI):** Elbette! Veri üretim scriptini `matplotlib` ve `seaborn` kütüphanelerini kullanarak görselleştirme yapacak şekilde güncelledim. Artık veri üretildiğinde otomatik olarak bir de dağılım grafiği (`visual_analysis.png`) oluşturuluyor.

Güncellenen `batarya_data.py` (üretilen kod) içeriği:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Görselleştirme ayarları
sns.set_theme(style="whitegrid")

# Veri Üretimi
n_rows = 500
screen_time = np.clip(np.random.normal(7, 1, n_rows), 0, 24)
battery_temp = np.clip(np.random.normal(35, 3, n_rows), 0, 100)

df = pd.DataFrame({
    'ID': np.arange(1, n_rows + 1),
    'Ekran_Suresi': np.round(screen_time, 2),
    'Batarya_Sicakligi': np.round(battery_temp, 2)
})

# CSV Kayıt
script_dir = os.path.dirname(__file__)
df.to_csv(os.path.join(script_dir, 'data.csv'), index=False)

# Görselleştirme (Grafik Kaydetme)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
sns.histplot(df['Ekran_Suresi'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Ekran Süresi Dağılımı (Saat)')
sns.histplot(df['Batarya_Sicakligi'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Batarya Sıcaklığı Dağılımı (°C)')

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'visual_analysis.png'))
print("Görselleştirme kaydedildi: visual_analysis.png")
```

---

**Öğrenci:** bu konuşmayı prompt.md şeklinde verir misin

**Yapay Zeka (AI):** Tüm bu süreci içeren `prompt.md` dosyasını hazırlıyorum.

---

**Öğrenci:** Şu anki prompt.md dosyası çok teknik bir rapor gibi görünüyor. Ben hocanınki gibi olmasını istiyorum. Lütfen prompt.md dosyasını şu formatta yeniden düzenle:

Öğrenci: (Benim sana verdiğim komutlar buraya gelecek)
Yapay Zeka (AI): (Senin verdiğin cevaplar ve yazdığın kodlar buraya gelecek)

Tüm konuşma geçmişimizi bu şekilde karşılıklı diyalog olarak yaz. Başlığını da 'Yapay Zeka ile Veri Üretimi ve Görselleştirme Örneği' yap.

**Yapay Zeka (AI):** Anladım! `prompt.md` dosyasını tamamen karşılıklı diyalog formatına getiriyorum ve tüm "Öğretmen" ifadelerini "Öğrenci" olarak güncelliyorum.
