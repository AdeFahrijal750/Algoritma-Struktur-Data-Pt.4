#buat program Fizzbuzz Tampilkan angka 1-100,
#Jika kelipatan 3, tampilkan "fizz". Jika kelipatan 5, Tampilakan "Buzz". 
#Jika kelipatan keduanya, tampilkan "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)