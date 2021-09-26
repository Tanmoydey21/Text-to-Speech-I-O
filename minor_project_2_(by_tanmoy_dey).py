# -*- coding: utf-8 -*-
"""Minor Project 2 (by Tanmoy Dey).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iuNMx-XHBxxs5VkVYO80SNfxkHNDrrAO
"""

# INSTALLING GOOGLE TEXT-TO-SPEECH 
! pip install gTTS

! pip install PyPDF2

# Import the required module for text to speech conversion 
from gtts import gTTS 
import PyPDF2

# Opening the PDF file
path = open('Python for Aspiring Data Scientists.pdf', 'rb')
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
  
# the page with which you want to start
# this will read the page of 2nd page.
from_page = pdfReader.getPage(2)
  
# extracting the text from the PDF
pdf = from_page.extractText()

# The text that you want to convert to audio 
mytext=pdf
print(mytext)
# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, tld='co.in', slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("Output.mp3")





