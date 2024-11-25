#Euler_Project_on_Python    #by Hay_VR
i=pow(2,1000)
sum=0
while i>0:
    sum+=i%10
    i=i//10
print(sum)