""" Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran
 bir fonksiyon yazın.(a <= 100,b <= 100)
 
 a2 + b2 =c2"""

def pisagor():
    liste=[]
    for a in range(1,101):
        for b in range(1,101):
                    c =((a**2)+(b**2))**0.5
                    if c==int(c):
                        liste.append((a,b,int(c)))
                        
                        
    
    return liste


    
    
print(pisagor())