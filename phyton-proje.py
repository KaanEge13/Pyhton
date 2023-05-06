"""1- Bir listeyi düzleştiren (flatten) fonksiyon yazin. 
#Elemanlari birden çok katmanli listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

    ##Örnek olarak:

  input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

    output: [1,'a','cat',2,3,'dog',4,5]
"""

sampleArray=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
newArray=[]
def f_Unpack(x):

    for i in x:
      if isinstance(i, list):
        f_Unpack(i)

      else:
         newArray.append(i)
         print("New output ",newArray)
f_Unpack(sampleArray)
print(newArray)

'''
2- Verilen listenin içindeki elemanlari tersine döndüren bir fonksiyon yazin. Eğer listenin içindeki elemanlar da liste içeriyorsa onlarin elemanlarini da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]         

'''

def reverse_list(n):
 n = n[::-1]
 n = [i[::-1] for i in n]
 return n

list1=[[1, 2], [3, 4], [5, 6, 7]]


print(reverse_list(liste1))


        
    





