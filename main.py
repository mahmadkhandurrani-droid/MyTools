
print("Hello, World!")
# main.py
import Text_utils
import Word_utils
import Number_utils

while True:
    print("\n--- MyTools Menu ---")
    print("1. Count vowels")
    print("2. Reverse sentence & count vowels")
    print("3. Find prime numbers")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        text = input("Enter text: ")
        total_v = Text_utils.count_vowels(text)
        print("Total vowels:", total_v)
        print("Primes up to total vowels:", Number_utils.find_primes(1, total_v))

    elif choice == "2":
        sentence = input("Enter sentence: ")
        rev, total_v = Word_utils.reverse_words(sentence)
        print("Reversed sentence:", rev)
        print("Total vowels:", total_v)
        print("Primes up to total vowels:", Number_utils.find_primes(1, total_v))

    elif choice == "3":
        start = int(input("Start of range: "))
        end = int(input("End of range: "))
        print("Prime numbers:", Number_utils.find_primes(start, end))

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
