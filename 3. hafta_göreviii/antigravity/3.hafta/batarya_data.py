import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Görselleştirme ayarları
sns.set_theme(style="whitegrid")

# Parametreler
n_rows = 500
mean_screen_time = 7
std_screen_time = 1
mean_temp = 35
std_temp = 3

# Normal dağılım ile veri üretimi
screen_time = np.random.normal(mean_screen_time, std_screen_time, n_rows)
battery_temp = np.random.normal(mean_temp, std_temp, n_rows)

# Mantıklı aralıklarda sınırlandırma
screen_time = np.clip(screen_time, 0, 24)
battery_temp = np.clip(battery_temp, 0, 100)

# Veri seti oluşturma
df = pd.DataFrame({
    'ID': np.arange(1, n_rows + 1),
    'Ekran_Suresi': np.round(screen_time, 2),
    'Batarya_Sicakligi': np.round(battery_temp, 2)
})

# CSV olarak kaydetme
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, 'data.csv')
df.to_csv(csv_path, index=False)
print(f"Veri seti başarıyla oluşturuldu: {csv_path}")

# Görselleştirme
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Ekran Süresi Dağılımı
sns.histplot(df['Ekran_Suresi'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Ekran Süresi Dağılımı (Saat)')
axes[0].set_xlabel('Saat')
axes[0].set_ylabel('Frekans')

# Batarya Sıcaklığı Dağılımı
sns.histplot(df['Batarya_Sicakligi'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Batarya Sıcaklığı Dağılımı (°C)')
axes[1].set_xlabel('Sıcaklık (°C)')
axes[1].set_ylabel('Frekans')

plt.tight_layout()
plot_path = os.path.join(script_dir, 'visual_analysis.png')
plt.savefig(plot_path)
print(f"Görselleştirme kaydedildi: {plot_path}")
# plt.show() # Terminalde çalışırken gerekirse aktif edilebilir