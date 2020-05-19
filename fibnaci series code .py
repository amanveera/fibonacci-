# program to dislplay fibonaci series

nterms = int(input(" number of terms needed"))

# first tw o terms
n1, n2 = 0, 1
count = 0

# check if the number of term is valid

if nterms <= 0:
    print ("please  enter a positive integer")
elif nterms == 1:
    print("faboncai series upto",nterms,":")
    print(n1)
else:
     print("faboncai sequence:")
     while count < nterms:
        print(n1)
        nth = n1 +n2

        #update values
        
        n1 = n2
        n2 = nth
        count += 1


        
