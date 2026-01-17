'''1. Pattern for 
***
***
***'''

'''def pattern(n):
    for i in range(0, n):
        for j in range(0, n):
            print("*", end = ' ')
        print()

pattern(3)'''

'''2. Pattern for 
* 
* * 
* * * '''

'''def pattern_diag(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end=' ')
        print()

pattern_diag(6)'''


'''3. Pattern for 
1 
2 2 
3 3 3 
4 4 4 4'''

'''def pattern_num(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(i+1, end=' ')
        print()

pattern_num(4)'''


'''4. Pattern for
1 
1 2 
1 2 3'''

def pattern_n(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print(j+1, end= ' ')
        print()

pattern_n(3)


'''5. Pattern for
* * * * 
* * * 
* * 
* '''

'''def pattern_strev(n):
    for i in range(0,n):
        for j in range(n-i, 0, -1):
            print("*", end=' ')
        print()

pattern_strev(4)'''


'''6. Pattern for 
1 2 3 
1 2 
1 '''

'''def pattern_numrev(n):
    for i in range(n):
        k = 0
        for j in range(i,n):
            print(k+1, end=' ')
            k += 1
        print()

pattern_numrev(5)'''


'''7. Pattern for
    *
   ***
  *****'''

'''def pattern_py(n):
  for i in range(1,n+1):
    for j in range(0,n-i):
       print(" ", end = "")
    for k in range(1, 2*i):
       print("*", end = "")
    print()
   
pattern_py(5)'''



'''8. Pattern for 
 *****
  ***
   *'''

'''def invpattern_py(n):
    for i in range(0, n):
        for j in range(0,i):
            print(" ", end = "")
        for k in range(0, 2*n - (2*i +1)):
            print("*", end="")
        print()

invpattern_py(4)'''


'''9. Pattern for 
   *
  ***
 *****
*******
*******
 *****
  ***
   *'''

'''def diamond(n):
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ", end = "")
        for k in range(1, 2*i):
            print("*", end = "")
        print()
    for i in range(0, n):
        for j in range(0,i):
            print(" ", end = "")
        for k in range(0, 2*n - (2*i +1)):
            print("*", end="")
        print()

diamond(4)'''

'''10. Pattern for
*
**
***
****
*****
****
***
**
*'''

'''def half_pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
    for i in range(1, n+1):
        for j in range(i, n):
            print("*", end="")
        print()

half_pyramid(5)'''