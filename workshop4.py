def perfect_number(number):
    total = 0
    for i in range(1,number):
       if number %i == 0:
          total +=i
number =int(input("Lütfen bir sayı giriniz:"))
if perfect_number(number):
    print(number,"mükemmel sayıdır")
else:
    print(number,"mükemmel sayı değildir")
