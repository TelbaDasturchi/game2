from uzwords import words
import random

# so'zlar listidan so'z ajratib oluvchi funksiya
def get_word():
    word = random.choice(words)

    # so'zda chiziqcha(-) yoki bo'shjoy( ) yoki krilcha("қ") harfi ('қ' klavyaturada mavjudmas)mavjut bo'lsa boshqa so'z generatsiya qilish
    while '-' in word or ' ' in word or 'қ' in word:
        word = random.choice(words)

    # so'zni qaytarish
    return word.upper()

# kiritilgan harflar royhatidagi harflar so'zda mavjudligini tekshiruvchi funksiya
def display(user_letters, word):

    # natijani yigish uchun bo'sh o'zgaruvchi olish (string)
    display_latter=''

    # so'zdagi harfalrni ajratib olib tekshirish
    for later in word:

        # agar harf kiritilgan harflar orasida mavjud bo'lsa, uni natijaga qo'shish
        if later in user_letters.upper():
            display_latter += later

        # agar mavjud bo'lmasa, o'rniga chiziqcha(-) ni natijaga qo'shish 
        else:
            display_latter += '-'
        
    # natijani qaytarish
    return display_latter

# asosiy funksiya ya'ni bo'laklarni birlashtirib turish
def play():
    # so'z tanlab olish
    word = get_word()

    # so'zdagi harfalrdan elementlari takrorlanmaydigan ro'yhat hosil qilish
    word_letters = set(word)

    # foydalanuvchi tomonidan kiritilgan belgilarni saqlovchi o'zgaruvchi olish
    user_letters = ''

    # foydalanuvchiga ma'lumot tanlangan so'z haqida chiqarish
    print(f"Men {len(word)} honali so'z o'yladim topaolasizmi? ")

    # so'zdagi harflar ro'yhati bo'shamaguncha ya'ni hamma harf topilmaguncha takrorlanuvchi sikl ochish 
    while word_letters:
        # sikl davomida har safar ma'lumot berish
        print(display(user_letters, word))

        # foydalanuvchi tomonidan kiritilgan harflar ro'yxatini bo'sh bo'lmasa konsolga chiqarish 
        if user_letters:
            print(f"Siz kiritgan harflar: {user_letters}")

        # foydalanuvchidan harf qabul qilish
        letter = input("Harf kiriting: ").upper()

        # kiritilgan harf oldin kiritilmaganiga tekshirish
        if letter in user_letters:

            # oldin kiritilganlik haqida habar chiqarish va siklni bir qadan o'tkazib yuborish
            print("Siz bu harfni oldin kiritgansiz!")
            continue
        if letter in word:

            # harf ro'yhatda mavjud bo'lsa so'zdagi harflar ro'yhatidan uni olib tashlash va to'g'ri ekanligi haqida habar chiqarish
            word_letters.remove(letter)
            print(f"{letter} harf to'g'ri")
        else:

            # kiritilgan harf so'zdagi harflar ro'yhatida bo'lmasa bu haqida habar chiqarish
            print("Bunday harf yo'q")

        # kiritilgan harfni harflar ro'yahtiga qo'shib quyish
        user_letters += letter
    
    # o'yindagi natija haqida habar chiqarish
    print(f"Tabriklayman! Siz {word} so'zini {len(user_letters)} o'rinishda topdingiz!")