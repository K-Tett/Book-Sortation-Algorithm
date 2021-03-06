# -*- coding: utf-8 -*-
"""Mini Project - Linux Pro

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N3wB_O9ze_vuqUK1w8z5eJ_NOW3ZU-r6
"""

"""
TODO:
- [ ] Import local files
- [ ] Make GUI to import csv files
- [ ] Add options to choose which sorting algorithm to go for
- [ ] Add more sortation
- [ ] Visualize the sortation
"""

from timeit import default_timer as time

"""
#When used with Google Colab to mount the Google Drive to the program
#make google colab connect to google drive
from google.colab import drive
drive.mount('/content/gdrive')

#give the directory of where the module is
import os, sys
sys.path.append('/content/gdrive/MyDrive/Colab Notebooks')

#python modules
import utils
import sorts

bookshelf = utils.load_book('/content/gdrive/MyDrive/Colab Notebooks/books_new - books_new.csv')
"""

####### Comparsion Functions #######
def by_title_ascending(book_a, book_b):
  return book_a['title_lowercase'] > book_b['title_lowercase']

def by_author_ascending(book_a, book_b):
  return book_a['author_lowercase'] > book_b['author_lowercase']

def by_genre_ascending(book_a, book_b):
  return book_a['genre_lowercase'] > book_b['genre_lowercase']

def by_total_length_of_book(book_a, book_b):
  return len(book_a['author_lowercase']) + len(book_a['title_lowercase']) > len(book_b['author_lowercase']) + len(book_b['title_lowercase'])

####### Outputs Functions #######

####### Bubble Sort #######
print(f"\n==== Bubble Sort - Title A-Z ====\n")
start = time() 
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_1:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes: \n", end - start, "s \n")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Bubble Sort - Title Z-A ====\n")
start = time()
sort_2 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes: \n", end - start, "s \n")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Bubble Sort - Author A-Z ====\n")
start = time()
sort_3 = sorts.bubble_sort(bookshelf, by_author_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_3:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes: \n", end - start, "s \n")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Bubble Sort - Author Z-A ====\n")
start = time()
sort_4 = sorts.bubble_sort(bookshelf, by_author_ascending)
sort_4.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes: \n", end - start, "s \n")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Bubble Sort - Genre A-Z ====\n")
start = time()
sort_3 = sorts.bubble_sort(bookshelf, by_genre_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_3:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Bubble Sort - Genre Z-A ====\n")
start = time()
sort_4 = sorts.bubble_sort(bookshelf, by_genre_ascending)
sort_4.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Bubble Sort - Total Length of Book (low to high) ====\n")
start = time()
sort_5 = sorts.bubble_sort(bookshelf, by_total_length_of_book)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Bubble Sort - Total Length of Book (high to low) ====\n")
start = time()
sort_6 = sorts.bubble_sort(bookshelf, by_total_length_of_book)
sort_6.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

####### Quick Sort #######
print(f"\n==== Quick Sort - Title A-Z ====\n")
start = time() 
sort_1_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_title_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_1_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:", end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Quick Sort - Title Z-A ====\n")
start = time()
sort_2_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_title_ascending)
sort_2_2.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_2_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Quick Sort - Author A-Z ====\n")
start = time()
sort_3_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_author_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_3_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Quick Sort - Author Z-A ====\n")
start = time()
sort_4_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_author_ascending)
sort_4_2.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_4_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Quick Sort - Genre A-Z ====\n")
start = time()
sort_5_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_genre_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_5_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Quick Sort - Genre Z-A ====\n")
start = time()
sort_6_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_genre_ascending)
sort_6_2.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_6_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Quick Sort - Total Length of Book (low to high) ====\n")
start = time()
sort_7_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_total_length_of_book)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_7_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Quick Sort - Total Length of Book (high to low) ====\n")
start = time()
sort_8_2 = sorts.quick_sort(bookshelf, 0, len(bookshelf) - 1, by_total_length_of_book)
sort_8_2.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_8_2:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

####### Selection Sort #######
print(f"\n==== Selection Sort - Title A-Z ====\n")
start = time() 
sort_1_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_title_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_1_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:", end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Selection Sort - Title Z-A ====\n")
start = time()
sort_2_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_title_ascending)
sort_2_4.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_2_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Selection Sort - Author A-Z ====\n")
start = time()
sort_3_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_author_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_3_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Selection Sort - Author Z-A ====\n")
start = time()
sort_4_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_author_ascending)
sort_4_4.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_4_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Selection Sort - Genre A-Z ====\n")
start = time()
sort_5_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_genre_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_5_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Selection Sort - Genre Z-A ====\n")
start = time()
sort_6_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_genre_ascending)
sort_6_4.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_6_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Selection Sort - Total Length of Book (low to high) ====\n")
start = time()
sort_7_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_total_length_of_book)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_7_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print(end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Selection Sort - Total Length of Book (high to low) ====\n")
start = time()
sort_8_4 = sorts.selection_sort(bookshelf, len(bookshelf), by_total_length_of_book)
sort_8_4.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_8_4:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

####### Insertion Sort #######
print(f"\n==== Insertion Sort - Title A-Z ====\n")
start = time() 
sort_1_5 = sorts.insertion_sort(bookshelf, by_title_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_1_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:", end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Insertion Sort - Title Z-A ====\n")
start = time()
sort_2_5 = sorts.insertion_sort(bookshelf, by_title_ascending)
sort_2_5.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_2_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "S")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Insertion Sort - Author A-Z ====\n")
start = time()
sort_3_5 = sorts.insertion_sort(bookshelf, by_author_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_3_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Insertion Sort - Author Z-A ====\n")
start = time()
sort_4_5 = sorts.insertion_sort(bookshelf, by_author_ascending)
sort_4_5.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_4_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Insertion Sort - Genre A-Z ====\n")
start = time()
sort_5_5 = sorts.insertion_sort(bookshelf, by_genre_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_5_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Insertion Sort - Genre Z-A ====\n")
start = time()
sort_6_5 = sorts.insertion_sort(bookshelf, by_genre_ascending)
sort_6_5.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_6_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Insertion Sort - Total Length of Book (low to high) ====\n")
start = time()
sort_7_5 = sorts.insertion_sort(bookshelf, by_total_length_of_book)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_7_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Insertion Sort - Total Length of Book (high to low) ====\n")
start = time()
sort_8_5 = sorts.insertion_sort(bookshelf, by_total_length_of_book)
sort_8_5.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_8_5:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

####### Heap Sort #######
print(f"\n==== Heap Sort - Title A-Z ====\n")
start = time() 
sort_1_6 = sorts.heap_sort(bookshelf, by_title_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_1_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:", end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Heap Sort - Title Z-A ====\n")
start = time()
sort_2_6 = sorts.heap_sort(bookshelf, by_title_ascending)
sort_2_6.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_2_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINSIHED ---")

print(f"\n==== Heap Sort - Author A-Z ====\n")
start = time()
sort_3_6 = sorts.heap_sort(bookshelf, by_author_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_3_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Heap Sort - Author Z-A ====\n")
start = time()
sort_4_6 = sorts.heap_sort(bookshelf, by_author_ascending)
sort_4_6.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_4_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Heap Sort - Genre A-Z ====\n")
start = time()
sort_5_6 = sorts.heap_sort(bookshelf, by_genre_ascending)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_5_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Heap Sort - Genre Z-A ====\n")
start = time()
sort_6_6 = sorts.heap_sort(bookshelf, by_genre_ascending)
sort_6_6.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_6_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Heap Sort - Total Length of Book (low to high) ====\n")
start = time()
sort_7_6 = sorts.heap_sort(bookshelf, by_total_length_of_book)
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_7_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

print(f"\n==== Heap Sort - Total Length of Book (high to low) ====\n")
start = time ()
sort_8_6 = sorts.heap_sort(bookshelf, by_total_length_of_book)
sort_8_6.reverse()
print('{:<55} | {:>23} | {:>10}\n'.format("Title of the book", "Author", "Genre"))
for book in sort_8_6:
  print('{:<55} | {:>23} | {:>10}'.format(book['Title'], book['Author'], book['Genre']))
end = time()
print("Sorting time takes:",end - start, "s")
print(f"--- SORTING FINISHED ---\n")

"""| |Bubble Sort |Quick Sort | Selection Sort | Insertion Sort | Heap Sort |
|-|-|-|-|-|-|
|Average time execution (seconds)|0.0369|0.0281| 0.0334 | 0.1731 |0.0333|
"""

# -*- coding: utf-8 -*-
"""sorts

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M6Rw33CbJqWZBwpTai3tJkBX9BMMQGv4
"""

#sorts.py module

import random

#optimized bubble sort algorithm
def bubble_sort(array, comparison_function_used):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(array) - 1):
      if comparison_function_used(array[idx], array[idx + 1]): #if left > right
        sorted = False
        array[idx], array[idx + 1] = array[idx + 1], array[idx] #swap function
        swaps += 1
  print("Bubble Sort: There were {0} swaps in the operation".format(swaps))
  return array

#random pivoted point quick sort algorithm
def partition(array, low, high, comparison_function_used):
    i = (low-1)         # index of smaller element
    pivot = array[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if comparison_function_used(pivot, array[j]):
  
            # increment index of smaller element
            i = i+1
            array[i], array[j] = array[j], array[i]
  
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quick_sort(array, low, high, comparison_function_used):
  if len(array) == 1:
    return array
  if low < high:
    pi = partition(array, low, high, comparison_function_used)

    quick_sort(array, low, pi-1, comparison_function_used)
    quick_sort(array, pi+1, high, comparison_function_used)
  return array

#selection sort algorithm (might be in reverse by default?)
def selection_sort(array, size, comparison_function_used):
  for step in range(size):
    min_index = step
    min_string = array[step]

    for i in range(step + 1, size):
      if comparison_function_used(min_string, array[i]):
        min_string = array[i]
        min_index = i
        
    if min_index != 1:
      array[step], array[min_index] = array[min_index], array[step]

  return array

#insertion sort algorithm
def insertion_sort(array, comparison_function_used):
  for step in range(1, len(array)):
    key = array[step]
    j = step - 1

    while j>=0 and comparison_function_used(array[j], key):
      array[j + 1] = array[j]
      j -= 1

    array[j+1] = key

  return array

#heap sorting algorithm
def heapify(array, n, i, comparison_function_used):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and comparison_function_used(array[l], array[i]):
    largest = l

  if r < n and comparison_function_used(array[r], array[largest]):
    largest = r
  
  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    heapify(array, n, largest, comparison_function_used)

  return array

def heap_sort(array, comparison_function_used):
  n = len(array)

  for i in range(n//2, -1, -1):
    heapify(array, n, i, comparison_function_used)

  for i in range(n-1, 0, -1):
    array[i], array[0] = array[0], array[i]
    heapify(array, i, 0, comparison_function_used)

  return array

# -*- coding: utf-8 -*-
"""utils.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16h5Xf4OSr-4jHxiW3aTBoWiD8ZHxhv41
"""

"""
script that load the book that the user called to open
then make the title of the book, author, and the genre lowercase.
return the naming as bookshelf
"""

import csv

#bookshelf data from the csv file
#credit: https://gist.github.com/jaidevd/23aef12e9bf56c618c41

def load_book(filename):
  bookshelf = []
  with open(filename, 'r') as file:
    shelf = csv.DictReader(file)
    for book in shelf:
      book['author_lowercase'] = book['Author'].lower()
      book['title_lowercase'] = book['Title'].lower()
      book['genre_lowercase'] = book['Genre'].lower()

      #update the bookshelf with new file list
      bookshelf.append(book)

  return bookshelf