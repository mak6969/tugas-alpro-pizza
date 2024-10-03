#menampilkan menu menu 
print ("Selamat Datang Di Pizza Hut")
print ("\nSilahkan Pilih Pizza Anda")
print ("1. Cheeseburger\t\t\tRp.60.000")
print ("2. Pepperoni\t\t\tRp.75.000")
print ("3. Frankfurter BBQ\t\tRp.65.000")
print ("4. American Favourite\t\tRp.70.000")
print ("5. Meat Lovers\t\t\tRp.80.000")
print ("Masukkan Nomor Pizza Pilihan Anda")

#variabel
pizza = int (input())
bill=0
harga_pizza = 0

#memilih menu
if pizza == 1:
    harga_pizza += 60000
    bill += harga_pizza
elif pizza == 2:
    harga_pizza += 75000
    bill += harga_pizza
elif pizza == 3:
    harga_pizza += 65000
    bill += harga_pizza
elif pizza == 4:
    harga_pizza += 70000
    bill += harga_pizza
elif pizza== 5:
    harga_pizza += 80000
    bill += harga_pizza
else:
    print("Pilihan Pizza Tidak Valid")

#menunjukkan jenis jenis ukuran pizza
print ("Pilih Ukuran Pizza Anda")
print ("1. Personal\t\t\tRp.10.000")
print ("2. Regular\t\t\tRp.40.000")
print ("3. Large\t\t\tRp.70.000")
print ("Masukkan Nomor Ukuran")
Size = int (input ())
harga_size = 0

if Size == 1:
    harga_size += 10000
    bill += harga_size
elif Size == 2:
    harga_size += 40000
    bill += harga_size
elif Size == 3:
    harga_size += 70000
    bill += harga_size
else:
    print("Ukuran Tidak Valid")

#variasi topping tambahan
print ("Pilih Topping Pizza Anda")
print ("1. Mozzarella Ekstra\t\tRp.10.000") 
print ("2. Keju Parmesan\t\tRp.10.000") 
print ("3. Daging Asap\t\t\tRp.18.000") 
print ("4. Saus Pasta\t\t\tRp.8.000") 
print ("5. Kacang Polong\t\tRp.10.000") 
print ("6. Serbuk Cabai\t\t\tRp.6.000")
print ("Masukkan Nomor Topping")
Topping = int (input ())
harga_topping = 0

if Topping == 1:
    harga_topping += 10000
    bill += harga_topping
elif Topping == 2:
    harga_topping += 10000
    bill += harga_topping
elif Topping == 3:
    harga_topping += 18000
    bill += harga_topping
elif Topping == 4:
    harga_topping += 8000
    bill += harga_topping
elif Topping == 5:
    harga_topping += 10000
    bill += harga_topping
elif Topping == 6:
    harga_topping += 6000
    bill += harga_topping
else:
    print("Topping Tidak Valid")

#memilih variasi crust
print ("Pilih Crust, Tidak Ada Biaya Tambahan Untuk Crust")
print("1. Pan Crust")
print("2. Thin Crust")
print("3. Stuffed Crust")
print("4. Cheese Crust")
print("5. Classic Crust")
print("6. Whole Wheat Crust")
print("Masukkan Nomor Crust")
Crust = input ()

#opsi menambahkan keju
print ("Ingin Menambah Keju Dengan Biaya Rp.10.000? (y/n)")
Keju = input ()
harga_keju = 0
if Keju == str ("y"):
    harga_keju += 10000
    bill += harga_keju
    print("\nTotal Pesanan Sedang Diproses")
else:
    print("\nTotal Pesanan Sedang Diproses")

print("\nTotal Keseluruhan Pesanan Anda")
print("Total keseluruhan Pesanan Anda: Rp.", bill)