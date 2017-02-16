#!/bin/python
def insertionSort(ar):  
    for i in range(len(ar)):
        current_value = ar[i]
        pos = i
        modYet = 0
        #print current_value, pos
        if pos > 0 and current_value > ar[pos - 1]:
            for i in range(len(ar) - 1):
                print ar[i],
            print ar[-1]
            
        while pos > 0 and current_value < ar[pos - 1]:
            modYet = 1
            ar[pos] = ar[pos - 1]
            pos -= 1

            if current_value > ar[pos - 1]:
                modYet = 0
                ar[pos] = current_value
                for i in range(len(ar) - 1):
                    print ar[i],
                print ar[-1]
                
        if pos == 0 and modYet == 1:
            #print pos, modYet
            ar[pos] = current_value
            for i in range(len(ar) - 1):
                print ar[i],
            print ar[-1]
            #print '$' 
        

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
