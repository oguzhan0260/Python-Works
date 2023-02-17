rakamlar=[0,1,2,3,4,5,6,7,8,9]

def faktöriyel_al(say):
    """ Bu fonksiyon girilen değerin faköriyelini alır.
    
    """
    x=1
    if say==0 and say==1:
        return 1
    else:
        while say>1:
            x*=say
            say-=1
    return x



def toplama (a,b,c):
    """ Bu fonksiyon girilen 3 tane değeri toplar."""
    return a+b+c


