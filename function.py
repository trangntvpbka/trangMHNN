import math; 
def giai_thua (n):
    if (n==0):
        gt=1; 
    if (n>0):
        i=1; 
        gt=1; 
        while (i<=n):
            gt=gt*i; 
            i+=1; 
    return gt; 
def tong(c,r,K):
    dem=1; 
    kq=1; 
    while (dem<=c-1):
        kq=kq+(math.pow(r,K)/giai_thua(K)); 
        dem+=1; 
    print (kq); 
    return kq; 
kq=tong(4,0.1,3); 
print(kq); 