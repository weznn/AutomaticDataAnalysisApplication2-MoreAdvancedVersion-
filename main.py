import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

def load_data():
    print("Veri giriş yöntemi seçin: \n1. CSV Yükle \n2. Excel Yükle")
    choice = input("Seçiminiz (1/2): ")
    if choice == "1":
        file_path = input("CSV dosyasının yolunu girin: ")
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
            print("Veri başarıyla yüklendi! İşte ilk 5 satır:")
            print(data.head())
            return data
        except Exception as e:
            print(f"Hata oluştu: {e}")
            return None
    elif choice == "2":
        file_path = input("Excel dosyasının yolunu girin: ")
        try:
            data = pd.read_excel(file_path)
            print("Veri başarıyla yüklendi! İşte ilk 5 satır:")
            print(data.head())
            return data
        except Exception as e:
            print(f"Hata oluştu: {e}")
            return None
    else:
        print("Geçersiz seçim!")
        return None

def suggest_analysis(data):
    print("Seçenekler: \n1. Tanımlayıcı İstatistikler \n2. Korelasyon Analizi \n3. Veri Dağılımı \n4. Histogram \n5. Kutu Grafiği \n6. Regresyon Analizi \n7. Normallik Testi")
    analysis_choice = input("Yapmak istediğiniz analiz türünü seçin (1-7): ")
    return analysis_choice

def perform_analysis(data, choice):
    if choice == "1":
        print("Tanımlayıcı İstatistikler:")
        print(data.describe())
    elif choice == "2":
        print("Korelasyon Matrisi:")
        numeric_data = data.select_dtypes(include=[np.number])
        if numeric_data.empty:
            print("Korelasyon analizi için yeterli sayısal veri yok!")
        else:
            print(numeric_data.corr())
            sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
            plt.show()
    elif choice == "3":
        data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
        plt.show()
    elif choice == "4":
        data.hist(figsize=(10, 6))
        plt.show()
    elif choice == "5":
        data.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
        plt.show()
    elif choice == "6":
        print("Regresyon analizi için bağımlı ve bağımsız değişkenleri belirtin.")
        x_column = input("Bağımsız değişken sütun adı: ")
        y_column = input("Bağımlı değişken sütun adı: ")
        if x_column in data.columns and y_column in data.columns:
            sns.regplot(x=data[x_column], y=data[y_column])
            plt.show()
        else:
            print("Geçersiz sütun isimleri!")
    elif choice == "7":
        column = input("Normallik testi yapmak istediğiniz sütun adını girin: ")
        if column in data.columns:
            stat, p = stats.shapiro(data[column].dropna())
            print(f"Shapiro-Wilk Testi: Test istatistiği={stat}, p-değeri={p}")
            if p > 0.05:
                print("Veri normal dağılıma uygun.")
            else:
                print("Veri normal dağılıma uymuyor.")
        else:
            print("Geçersiz sütun ismi!")
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        analysis_type = suggest_analysis(df)
        perform_analysis(df, analysis_type)
