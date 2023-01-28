print("*"*15,"Faktöriyel Bulma Programı","*"*15)

while True:

    say= int(input("faktöriyelini alınmasını istediniz sayı:\nÇıkmak için q basınız"))
    i=1
    faktöriyel=1
    if say <0:
        print("negatif sayı girdiniz. Tekar deneyin.")
        continue
    while i<say :
        i+=1
        faktöriyel *=i
    
    print(say,"Sayısının Faktöriyeli:",faktöriyel,"\n","*"*80)

