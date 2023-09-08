import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Excel dosyasını oku
eşleşen_df = pd.read_excel('eşleşen_ürünler.xlsx')

# Streamlit uygulamasını başlat
st.title("Şarküteri Ürünü Analizi")

# Ürün seçimini kullanıcıya bırak
urun_secim = st.selectbox("Ürün Seçin", eşleşen_df['Açıklama'])

# Seçilen ürünü filtrele
secilen_urun = eşleşen_df[eşleşen_df['Açıklama'] == urun_secim].iloc[0]

# İlgili yılların miktarlarını ve açıklamayı al
miktar_2022 = secilen_urun['2022']
miktar_2023 = secilen_urun['2023']
aciklama = secilen_urun['Açıklama']

# Artış veya azalışı hesapla
artis_azalis = miktar_2023 - miktar_2022
renk = 'green' if artis_azalis > 0 else 'red'

# Verileri bir çubuk grafikte göster
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(['2022', '2023'], [miktar_2022, miktar_2023], color=['blue', 'green'])
ax.text('2022', miktar_2022, str(miktar_2022), ha='center', va='bottom', fontsize=12)
ax.text('2023', miktar_2023, str(miktar_2023), ha='center', va='bottom', fontsize=12)
ax.set_xlabel('Yıl')
ax.set_ylabel('Miktar')
ax.set_title(f'{aciklama} Ürününün 2022 ve 2023 Miktar Karşılaştırması')
ax.bar('Artış/Azalış', artis_azalis, color=renk)
ax.text('Artış/Azalış', artis_azalis, f'{artis_azalis} ({artis_azalis/miktar_2022:.2%})', ha='center', va='bottom', fontsize=12)
ax.tick_params(axis='x', rotation=45)

# Streamlit uygulamasını çalıştır
st.pyplot(fig)

st.sidebar.text(f"{aciklama} Ürününün 2022 Miktarı: {miktar_2022}")
st.sidebar.text(f"{aciklama} Ürününün 2023 Miktarı: {miktar_2023}")
st.sidebar.text(f"Artış/Azalış: {artis_azalis} ({artis_azalis/miktar_2022:.2%})")
