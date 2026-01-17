'''11. Pattern for 
1 
0 1 
1 0 1''' 

'''def zeroone(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            val = 1
        else:
            val = 0
        for j in range(i, 2*i):
            print(val, end = " ")
            val = 1 - val
        print()

zeroone(6)'''

'''12. Pattern for 
1    1
12  21
123321'''

'''def righttri(n):
    for i in range(1, n+1):
        val = 1
        for j in range(1, i+1):
            print(j, end = "")
            val += 1
        for k in range(0, 2*(n-i)):
            print(" ", end = "")
        for l in range(i, 0, -1):
            print(l, end="")
        print()

righttri(5)'''

'''13. Pattern for 
1 
2 3 
4 5 6 
7 8 9 10''' 

'''def cont_numtri(n):
    val = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(val, end= " ")
            val+=1
        print()

cont_numtri(2)'''

'''14. Pattern for
A 
A B 
A B C 
A B C D '''

'''def alpha(n):
    val = 65
    for i in range(0, n):
        for j in range(0, i+1):
            print(chr(val), end = " ")
            val += 1
        print()
        val = 65

alpha(5)'''

'''15. Pattern for 
A B C D 
A B C 
A B 
A '''

'''def alpha_rev(n):
    val = 65
    for i in range(0, n):
        for j in range(i, n):
            print(chr(val), end = " ")
            val += 1
        print()
        val = 65

alpha_rev(5)'''

'''16. Pattern for 
A 
B B 
C C C'''

'''def alp_same(n):
    val = 65
    for i in range(0, n):
        for j in range(0, i+1):
            print(chr(val), end = " ")
        print()
        val += 1

alp_same(3)'''

'''17. Pattern for 
   A
  ABA
 ABCBA
ABCDCBA'''

'''def alp_pyr(n):
    for i in range(n):
        for j in range(0, n-i-1):
            print(" ", end = "")
        for j in range(i + 1):
            print(chr(65 + j), end="")
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end="")
        print()

alp_pyr(4)'''

'''18. Pattern for 
E
DE
CDE
BCDE
ABCDE'''

'''def des(n):
    for i in range(n):
        val = 69
        for j in range(0, i+1):
            print(chr(val-i), end= "")
            val += 1
        print()

des(5)'''

'''19. Pattern for
******
**  **
*    *
*    *
**  **
******'''

'''def star_diam(n):
    for i in range(0, n):
        for j in range(i, n):
            print("*", end = "")
        for k in range(0, 2*i):
            print(" ", end = "")
        for j in range(i, n):
            print("*", end = "")
        print()  
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end = "")
        for k in range(0, 2* (n-i-1)):
            print(" ", end = "")
        for j in range(0, i+1):
            print("*", end = "")
        print()

star_diam(3)'''

'''20. Pattern for 
*      *
**    **
***  ***
********
***  ***
**    **
*      *'''

'''def tri4nos(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end = "")
        for k in range(0, 2* (n-i-1)):
            print(" ", end = "")
        for j in range(0, i+1):
            print("*", end = "")
        print()
    for i in range(0, n):
        for j in range(i+1, n):
            print("*", end = "")
        for k in range(0, 2+(2*i)):
            print(" ", end = "")
        for j in range(i+1, n):
            print("*", end = "")
        print()

tri4nos(10)'''

'''21. Pattern for 
****
*  *
*  *
****'''

'''def rectangle(n):
    for i in range(0, n):
        if i == 0 or i == n-1:
            for j in range(0,n):
                print("*", end = "")
            print()
        else:
            for k in range(0,1):
                print("*", end = "")
            for l in range(0, n-2):
                print(" ", end = "")
            for k in range(0,1):
                print("*", end= "")
            print()

rectangle(4)'''

'''22. Pattern for 
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 '''

'''def numpattern(n):
    size = 2 * n - 1
    for i in range (size):
        for j in range (size):
            min_dis = min(i, j, size-1-i, size-1-j)
            print(n - min_dis, end = " ")
        print()

numpattern(4)'''

'''23. Pascal's triangle
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
1 5 10 10 5 1 '''

def pascal(n):
    for i in range(n):
        for j in range(i, n-1):
            print(' ', end = '')
        num = 1
        for j in range(0, i+1):
            print(num, end = ' ')
            num = num * (i-j) // (j+1)
        print()

pascal(5)