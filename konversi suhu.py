#konversi suhu dari celcius ke Fahrenheit, Kelvin & Reamur
#input
celcius = float(input('Enter suhu celcius :'))
print('suhu celcius adalah',celcius, "Celcius")

#rumus konvensi suhu
Fahrenheit = (celcius * (9/5)) + 32
Kelvin = (celcius + 273)
Reamur = (celcius + (4/5))

#print
print("--suhu dalam fahrenheit adalah",Fahrenheit, "Fahrenheit")
print("--suhu dalam kelvin adalah",Kelvin, "Kelvin")
print("--suhu dalam reamur adalah",Reamur, "Reamur")
print('jika ada yg salah mohon maaf')