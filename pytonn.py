def calculate_average(numbers):
   
    #Функція для обчислення середнього значення списку чисел.

    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def is_prime(number):
 
    #Функція для перевірки, чи є число простим.

    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_vowels(string):

    #Функція для підрахунку кількості голосних букв у рядку.

    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

def gcd(a, b):
    
    #Функція для знаходження найбільшого спільного дільника (НСД) двох чисел.

    while b != 0:
        a, b = b, a % b
    return a
