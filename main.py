import function ; 
import Hethong; 
import math; 
print ("Nhập vào số server có trong hệ thống:"); 
server=int(input()); 
print ("Nhập vào khả năng phục vụ của server:"); 
K=int(input()); 
print("Cường độ dòng vào:"); 
ld=int(input()); 
print ("Cường độ dòng ra:"); 
nuy=int(input()); 
if (server==1):
    Hethong.Mot(ld,nuy,K); 
if (server>1):
    Hethong.Nhieu (ld,nuy,server,K); 