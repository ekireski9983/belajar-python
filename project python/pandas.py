'''
*Data Analyst Project: Business Decision Research
Market Research and Recommendation and Visualization Technique for Business Decision Making - Part 1

Toko yang menjual berbagai kebutuhan olahraga seperti Jaket, Baju, Tas, dan Sepatu.
Toko ini mulai berjualan sejak tahun 2013, sehingga sudah memiliki pelanggan tetap sejak lama, dan
tetap berusaha untuk mendapatkan pelanggan baru sampai saat ini.
Di awal tahun 2019, manajer toko tersebut merekrut junior DA untuk membantu  memecahkan masalah yang ada di tokonya,
yaitu menurunnya pelanggan yang membeli kembali ke tokonya.
Junior DA tersebut pun diberi kepercayaan mengolah data transaksi toko tersebut.
Manajer toko mendefinisikan bahwa customer termasuk sudah bukan disebut pelanggan lagi (churn) ketika
dia sudah tidak bertransaksi ke tokonya lagi sampai dengan 6 bulan terakhir dari update data terakhir yang tersedia.
Manajer toko pun memberikan data transaksi dari tahun 2013 sampai dengan 2019 dalam bentuk
csv (comma separated value) dengan data_retail.csv dengan jumlah baris 100.000 baris data.

Field yang ada pada data tersebut antara lain:
1.No
2.Row_Num
3.Customer_ID
4.Product
5.First_Transaction
6.Last_Transaction
7.Average_Transaction_Amount
8.Count_Transaction

Market Research and Recommendation and Visualization Technique for Business Decision Making - Part 2

1. Data preparation test
--> Importing data: Melakukan import data_retail.csv ke python environment.
--> Cleansing data: Melakukan pembersihan dan modifikasi data sehingga siap digunakan untuk analisis lebih lanjut.
2. Data visualization test: Mendapatkan insight dari hasil visualisasi yang telah dibuat.
3. Basic stats method test: Mendapatkan insight dari model dan evaluasi model yang sudah dibuat dan diuji.
'''
#Importing Data dan Inspection
#Importlah dataset dari
'''
https://storage.googleapis.com/dqlab-dataset/data_retail.csv dan kemudian inspeksilah dataset tersebut dengan
'''
#1. mencetak lima data teratas saja,
#2. mencetak info dataset.

import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/data_retail.csv', sep=';')
print('Lima data teratas:')
print(df.head())
print('\nInfo dataset:')
print(df.info())

#Data Cleansing
#Dua kolom yang menunjukkan terjadinya transaksi tidak bertipe datetime, maka ubahlah kedua kolom tersebut ke tipe data datetime.
#Kemudian cetaklah kembali 5 data teratas dari dataframe df dan juga tipe data masing-masing kolomnya.
# Kolom First_Transaction
df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit='s', origin='1970-01-01')
# Kolom Last_Transaction
df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit='s', origin='1970-01-01')
print('Lima data teratas:')
print(df.head())
print('\nInfo dataset:')
print(df.info())

#Churn Customers
#Untuk menentukan churn customers sesuai definisi yang telah diberikan, carilah
#1. transaksi paling terakhir kapan dilakukan
#2. klasifikasikanlah mana customer yang berstatus churn dan mana yang tidak.
#Setelah itu cetak lima data teratas dan informasi dataset.
# Pengecekan transaksaksi terakhir dalam dataset
print(max(df['Last_Transaction']))

# Klasifikasikan customer yang berstatus churn atau tidak dengan boolean
df.loc[df['Last_Transaction']<='2018-08-01','is_churn'] = True
df.loc[df['Last_Transaction']>'2018-08-01', 'is_churn'] = False
#display
print('Lima data teratas:')
print(df.head())
print('\nInfo dataset:')
print(df.info())

#Menghapus kolom yang tidak diperlukan pada row num
del df['no']
del df['Row_Num']
# Cetak lima data teratas
print(df.head())

#Customer acquisition by year
#visualisasi data berupa trend of customer acquisition by year dengan meggunakan bar chart.
# Untuk itu buatlah feature/kolom tambahan yang merupakan tahun dari First_Transaction dan tahun dari Last_Transaction
# masing-masingnya dengan nama Year_First_Transaction dan Year_Last_Transaction sebelum melakukan visualisasi.
import matplotlib.pyplot as plt

# Kolom tahun transaksi pertama
df['Year_First_Transaction'] = df['First_Transaction'].dt.year
# Kolom tahun transaksi terakhir
df['Year_Last_Transaction'] = df['Last_Transaction'].dt.year

df_year = df.groupby(['Year_First_Transaction'])['Customer_ID'].count()
df_year.plot(x='Year_First_Transaction', y='Customer_ID', kind='bar', title='Graph of Customer Acquisition')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

#Transaction by year
#Visualisasikanlah trend jumlah transaksi per tahunnya dengan menggunakan bar chart.
import matplotlib.pyplot as plt
plt.clf()#clear current figure
df_year = df.groupby(['Year_First_Transaction'])['Count_Transaction'].sum()
df_year.plot(x='Year_First_Transaction', y='Count_Transaction', kind='bar', title='Graph of Transaction Customer')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Transaction')
plt.tight_layout()
plt.show()

#Average transaction amount by year
#Dengan menggunakan seaborn pointplot,
#visualisasikanlah tren dari tahun ke tahun rata-rata jumlah transaksi untuk tiap-tiap produknya.
import matplotlib.pyplot as plt
import seaborn as sns

plt.clf()
sns.pointplot(
   data = df.groupby(['Product', 'Year_First_Transaction']).mean().reset_index(),
   x='Year_First_Transaction',
   y='Average_Transaction_Amount',
   hue='Product'
            )
plt.tight_layout()
plt.show()

#Proporsi churned customer untuk setiap produk
#Dari sisi churned customer, khususnya untuk melihat seberapa besar proporsi churned customer untuk tiap-tiap produk dapat
#diketahui insight-nya melalui pie chart.
#Visualisasikan pie chartnya untuk keempat produk yang dimaksudkan.
import matplotlib.pyplot as plt

plt.clf()
# Melakukan pivot data dengan pivot_table
df_piv = df.pivot_table(
   index='is_churn',
   columns='Product',
   values='Customer_ID',
   aggfunc='count',
   fill_value=0)
# Mendapatkan Proportion Churn by Product
plot_product = df_piv.count().sort_values(ascending=False).head(5).index
# Plot pie chartnya
df_piv = df_piv.reindex(columns=plot_product)
df_piv.plot.pie(
   subplots=True,
   figsize=(10, 7),
   layout=(-1, 2),
   autopct='%1.0f%%',
   title='Proportion Churn by Product'
               )
plt.tight_layout()
plt.show()

#Distribusi kategorisasi count transaction
import matplotlib.pyplot as plt

plt.clf()
# Kategorisasi jumlah transaksi
def func(row):
   if row['Count_Transaction'] == 1:
      val = '1. 1'
   elif (row['Count_Transaction']>1 and row['Count_Transaction']<=3):
      val ='2. 2-3'
   elif (row['Count_Transaction']>3 and row['Count_Transaction']<=6):
      val ='3. 4-6'
   elif (row['Count_Transaction']>6 and row['Count_Transaction']<=10):
      val ='4. 7-10'
   else:
      val ='5. >10'
   return val
# Tambahkan kolom baru
df['Count_Transaction_Group'] = df.apply(func, axis=1)
#visualisasi
df_year = df.groupby(['Count_Transaction_Group'])['Customer_ID'].count()
df_year.plot(x='Count_Transaction_Group', y='Customer_ID', kind='bar', title='Customer Distribution by Count Transaction Group')
plt.xlabel('Count_Transaction_Group')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

#Distribusi kategorisasi average transaction amount
import matplotlib.pyplot as plt

plt.clf()
# Kategorisasi rata-rata besar transaksi
def f(row):
   if (row['Average_Transaction_Amount'] >= 100000 and row['Average_Transaction_Amount'] <=200000):
      val ='1. 100.000 - 250.000'
   elif (row['Average_Transaction_Amount'] >250000 and row['Average_Transaction_Amount'] <= 500000):
      val ='2. >250.000 - 500.000'
   elif (row['Average_Transaction_Amount'] >500000 and row['Average_Transaction_Amount'] <= 750000):
      val ='3. >500.000 - 750.000'
   elif (row['Average_Transaction_Amount'] >750000 and row['Average_Transaction_Amount'] <= 1000000):
      val ='4. >750.000 - 1.000.000'
   elif (row['Average_Transaction_Amount'] >1000000 and row['Average_Transaction_Amount'] <= 2500000):
      val ='5. >1.000.000 - 2.500.000'
   elif (row['Average_Transaction_Amount'] >2500000 and row['Average_Transaction_Amount'] <= 5000000):
      val ='6. >2.500.000 - 5.000.000'
   elif (row['Average_Transaction_Amount'] >5000000 and row['Average_Transaction_Amount'] <= 10000000):
      val ='7. >5.000.000 - 10.000.000'
   else:
      val='8. >10.000.000'
      return val
# Tambahkan kolom baru
df['Average_Transaction_Amount_Group'] = df.apply(f, axis=1)

df_year = df.groupby(['Average_Transaction_Amount_Group'])['Customer_ID'].count()
df_year.plot(x='Average_Transaction_Amount_Group', y='Customer_ID', kind='bar', title='Customer Distribution by Average Transaction Amount Group')
plt.xlabel('Average_Transaction_Amount_Group')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

#Feature Columns dan Target
#Di bagian ini, selanjutnya akan menentukan feature columns dari dataset yang dimiliki,
#di sini dipilih kolom Average_Transaction_Amount, Count_Transaction, dan Year_Diff.
#Akan tetapi, kolom terakhir belum ada. Silakan dicreate dahulu kolom Year_Diff ini dan kemudian
# assign dataset dengan feature columns ini sebagai variabel independent X.
#Untuk target tentunya persoalan costumer dengan kondisi churn atau tidak,
#assign dataset untuk target ini ke dalam variabe dependent y.
# Feature column: Year_Diff
df['Year_Diff'] = df['Year_Last_Transaction'] - df['Year_First_Transaction']
# Nama-nama feature columns
feature_columns = ['Average_Transaction_Amount', 'Count_Transaction', 'Year_Diff']
# Features variable
X = df[feature_columns]
# Target variable
y = df['is_churn']

#Split X dan y ke dalam bagian training dan testing
#Setelah variabel independent X dan variabel dependent y selesai dilakukan,
#maka pecahlah X dan y ke dalam bagian training dan testing. Bagian testing 25% dari jumlah entri data.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

#Train, predict dan evaluate
#Langkah selanjutnya akan membuat model menggunakan
#Linear Regression, inisialisasilah model, fit, dan kemudian evaluasi model dengan menggunakan confusion matrix.
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Inisiasi model logreg
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train, y_train)

# Predict model
y_pred = logreg.predict(X_test)

# Evaluasi model menggunakan confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', cnf_matrix)

#Visualisasi Confusion Matrix
#Confusion matrix yang telah dihitung sebelumnya dapat divisualisasikan dengan menggunakan heatmap dari seaborn.
#Untuk itu tampilkanlah visualisasi dari confusion matrix ini.
# import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.clf()
# name  of classes
class_names = [0, 1]
fig, ax = plt.subplots()

tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap='YlGnBu', fmt='g')
ax.xaxis.set_label_position('top')
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.tight_layout()
plt.show()

#Accuracy, Precision, dan Recall
#Kemudian, hitunglah nilai accuracy, precission dan
# recall berdasarkan nilai target sesungguhnya dan nilai target hasil prediksi.
from sklearn.metrics import accuracy_score, precision_score, recall_score

#Menghitung Accuracy, Precision, dan Recall
print('Accuracy :', accuracy_score(y_test,y_pred))
print('Precision:', precision_score(y_test, y_pred, average='micro'))
print('Recall   :', recall_score(y_test, y_pred, average='micro'))