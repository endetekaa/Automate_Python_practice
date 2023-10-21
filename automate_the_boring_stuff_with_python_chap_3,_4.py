# -*- coding: utf-8 -*-
"""Automate the boring Stuff with Python chap 3, 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fa9KLnWBQuvMSvw91okwKCY3CdTPsvAM
"""

def hello():
  print('What is your name?')
  name = input()
  print('Howdy! '+ name)
  print('Howdy!!! ' + name)
  print('Hello there! ' + name)
hello()

print('Hello', end = '')
print('World!')

print('dog', 'cat', 'mouse')
print('dog', 'cat', 'mouse', sep='ABC')

def plusOne(number):
  return number + 1
newNumber = plusOne(5)
print(newNumber)

def spam():
  eggs = 99
  print(eggs)
spam()

def spam():
  eggs = 99
  bacon()
  print(eggs)

def bacon():
  ham = 101
  eggs = 0

spam()

def spam():
  eggs = 'Hello'
  print(eggs)

eggs = 42
spam()
print(eggs)

def spam():
  global eggs
  eggs = 'Hello'
  print(eggs)

eggs = 42
spam()
print(eggs)

def div42by(divideBy):
  try:
    return 42/ divideBy
  except ZeroDivisionError:
    print('Error: You tried to divide by zero.')
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
try:
  numCat = input()
  if int(numCat) >= 4:
    print('That is a lot of cats')
  else:
    print('That is not that many cats.')
except:
  print('You did not enter a number.')