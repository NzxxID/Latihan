# a = 10, a adalah variabel dengan nilai 10

# Tipe Data : Angka Satuan (integer)
data_integer = 10
print("data :", data_integer)
print("bertipe", type(data_integer))

# Tipe Data : angka dengan koma (float)
data_float = 1.5
print("data :", data_float)
print("bertipe", type(data_float))

# Tipe Data : kumpulan karakter (String)
data_string = "Naufal"
print("data :", data_string)
print("bertipe", type(data_string))

# Tipe Data : Biner True/False (Boolean)
data_bool = False
print("data :", data_bool)
print("bertipe", type(data_bool))

## Tipe Data Khusus 

# Bilangan Kompleks
data_complex = complex(5,6) 
print("data :", data_complex)
print("bertipe", type(data_complex))

# Tipe data dari Bahasa C 
from ctypes import c_double

data_c_double = c_double(10.5)

print("data :", data_c_double)
print("bertipe", type(data_c_double))

