"""
Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
 Bu işlemi *continue* ile yapmaya çalışın."""


i=None
list=[*range(0,101)]
for i in list:
    if i %3 !=0:
        continue
    print(i)


