# Python Program to Check Prime Number

def PrimeChecker(a):  
   
    if a > 1:  
        
        for j in range(2, int(a/2) + 1):  
           
            if (a % j) == 0:  
                print(a, "is not a prime number")  
                break  
   
        else:  
            print(a, "is a prime number")  
   
    else:  
        print(a, "is not a prime number")  

a = int(input("Enter an input number:"))  

PrimeChecker(a) 