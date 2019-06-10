import math; 
import function; 
def Mot (ld,nuy,K):
    p=ld/nuy; 
    if (p!=1):
        p0=(1-p)/(1-math.pow(p,K+1)); 
    if (p==1):
        p0=1/(K+1); 
    list_ppd=[p0]; 
    dem=1 ; 
    while (dem<=K):
        list_ppd.append((math.pow(p,dem)*p0)); 
        dem+=1; 
    if (p!=1):
        L=(p*(1+K*math.pow(p,K+1)-(K+1)*math.pow(p,K)))/((1-p)*(1-math.pow(p,K+1))); 
        Lq=L-((p*(1-math.pow(p,K)))/(1-math.pow(p,K+1))); 
        V=(p/(1-math.pow(p,K+1))*math.pow((1-p),2))*(1+p-math.pow((K+1),2)*math.pow(p,K)+(2*K*K+2*K-1)*math.pow(p,K+1)-K*K*math.pow(p,K+2))-L*L; 
    if (p==1):
        L=K/2; 
        Lq=(K*(K-1))/(2*(K-1)); 
        V=(K*(K+2))/12; 
    Vq=V-p0*(L+Lq); 
    print ("Phân phối dừng của hệ thống là:"); 
    print (list_ppd); 
    print ("Số khách hàng trung bình trong hàng đợi là:",Lq); 
    print ("Số khách hàng trung bình trong hệ thống là:",L); 
    print ("Thời gian đợi trung bình trong hệ thống là:",V); 
    print ("Thời gian đợi trung bình trong hàng đợi là:",Vq); 
    return ; 
def Nhieu (ld,nuy,server,K):
    r=ld/nuy; 
    p=r/server; 
    gt=function.giai_thua(server); 
    t=function.tong(server,r,K); 
    p0=1/(t+(server*math.pow(r,server))/(gt*(server-r))); 
    list_ppd=[p0]; 
    dem=1; 
    while (dem<=K):
        if (dem<=server-1):
            list_ppd.append((p0*math.pow(r,dem))/function.giai_thua(dem)); 
            dem+=1; 
        if (dem>=server and dem<=K):
            list_ppd.append((p0*math.pow(r,dem))/(math.pow(server,dem-server)*gt)); 
            dem+=1; 
    print ("Phân phối dừng của hệ thống là:"); 
    print (list_ppd); 
    Lq=(p0*math.pow(r,server)*p)/(gt*math.pow((1-p),2)); 
    print ("Số khách hàng trung bình trong hàng đợi là:",Lq); 
    L=Lq+r; 
    print ("Số khách hàng trung bình trong hệ thống là:",L); 
    E=(2*p0*math.pow(r,server))/(nuy*nuy*server*server*gt*math.pow(1-p,3)); 
    print ("Thời gian đợi trung bình trong hệ thống là:",E); 
    return; 