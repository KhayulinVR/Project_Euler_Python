#Euler_Project_on_Python    #by Hay_VR
x=0
sumkv=0
kvsum=0
while x<100:
    x+=1
    sumkv+=x*x
    kvsum+=x
kvsum=kvsum*kvsum
sumkv=sumkv-kvsum
print(-sumkv)