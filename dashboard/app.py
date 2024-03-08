import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

data_day = pd.read_csv('data/day.csv')

def visualisasi_musim_peminjam(data):
    musim_peminjam = data.groupby('season')['cnt'].sum().reset_index()

    # Visualisasi dengan sumbu y dibatasi pada rentang 0 - 1.500.000
    fig, ax = plt.subplots()
    ax.bar(musim_peminjam['season'], musim_peminjam['cnt'], color=['green', 'yellow', 'brown', 'skyblue'])
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Peminjam Sepeda')
    ax.set_title('Jumlah Peminjam Sepeda per Musim')
    ax.set_xticks(musim_peminjam['season'])
    ax.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    ax.set_ylim(0, 1500000)  # Menentukan rentang sumbu y
    st.pyplot(fig)

def visualisasi_scatter_suhu(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=data, alpha=0.6, ax=ax)
    ax.set_title('Hubungan antara Suhu dan Jumlah Penyewaan Sepeda')
    ax.set_xlabel('Temperatur')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.grid(True)
    st.pyplot(fig)

def main():
    st.title('Dashboard Visualisasi Data Bike Sharing')

    # Menampilkan visualisasi musim peminjam
    st.subheader('Visualisasi Jumlah Peminjam Sepeda per Musim')
    visualisasi_musim_peminjam(data_day)

    # Menampilkan visualisasi scatter plot suhu vs jumlah penyewaan
    st.subheader('Scatter Plot Suhu vs Jumlah Penyewaan Sepeda')
    visualisasi_scatter_suhu(data_day)

if __name__ == '__main__':
    main()