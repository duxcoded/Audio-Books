# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 08:55:51 2021
AudioBooks
@author: duxcode
"""
import pyttsx3
import PyPDF2


#Mở audio book. PDF dịnh dạng là binary nên ta dùng rb = read binary
book =  open("se.pdf", "rb")

#Goi thư viện PDF2 để đoc file PDF
pdfreader = PyPDF2.PdfFileReader(book)

#Đếm số trang của file
pages = pdfreader.numPages
print(pages)

#Setup pyttsx3 cơ bản
##Tạo object bot
bot = pyttsx3.init()
##Tạo object voices và lấy tất cả giọng nói trong máy ra
voices = bot.getProperty("voices")
##Chọn giọng cho voices: 0 nam; 1 nữ
bot.setProperty("voice", voices[1].id)
##Đọc từng trang cụ thể
# page = pdfreader.getPage(9)
#Lấy text từ file pdf để đọc
# text = page.extractText()
# bot.say(text)
# bot.runAndWait()


#Đọc từ rang 106 đến hết sách. Ta tạo object pages ở trên để làm việc này
for num in range(106, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()
