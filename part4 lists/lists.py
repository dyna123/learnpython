Data = [1, 4, 9, 16, 25, 36, 49, 64]

# Mengakses list
Subdata1 = Data[3]
Subdata2 = Data[-3]

# Memotong list
Subdata3 = Data[2:4]
Subdata4 = Data[:4]

Data2 = [100, 200, 300, 400, 500, 600, 700]

# Menambah list
Data3 = Data + Data2

# Merubah content dari list
Data[4] = 87

# Mengcopy list ke variabel baru
a = Data[:]
a[4] = 87

# Merubah content list dengan metode slicing
Data[1:2] = [3, 5]

# List dalam list
x = [Data, Data2]

# Mengakses list dalam multidimensi list
y = x[1][4]

# Method untuk list
Data.append(30)

# function untuk menggunakan list
panjang_list = len(Data)

print(Data)
print(panjang_list)
