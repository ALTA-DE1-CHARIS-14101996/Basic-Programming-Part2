'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
#Import Module
import locale

# Set locale sesuai dengan konvensi negara yang Anda inginkan (Indonesia)
locale.setlocale(locale.LC_ALL, 'id_ID')

#input harga
harga_awal = int(input("Input Harga:"))
diskon = int(input("Input Diskon:"))

#Membuat rumus harga setelah diskon
final_price = harga_awal-(harga_awal*(diskon/100))

#Mengubah hasil agar menjadi bentuk yang diinginkan
format_price = locale.format_string("%.0f", final_price, grouping=True)

#Output
print("harga yang harus dibayar adalah Rp.",format_price)