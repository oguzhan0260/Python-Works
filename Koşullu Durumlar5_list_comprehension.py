liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]

# yeni_liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

yeni_liste =list()

yeni_liste= [x for i in liste for x in i]

print(yeni_liste)
