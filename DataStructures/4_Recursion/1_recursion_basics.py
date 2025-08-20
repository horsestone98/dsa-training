# Recursion basic problems
# 1. Sum of 'n' numbers

# def sumnumbers(n):
#         if n == 0:
#             return 0
#         else:
#             return n + sumnumbers(n-1)

# print(sumnumbers(5))

# 2. Printing a name for 'n' times
# def print_name(name, n):
#     if n <= 0:
#         return 
#     print(name)
#     print_name(name, n - 1)

# # Example usage
# print_name("Kailash", 5)

# 3. Printing 1 to N

# def print_numbers(i, n):
#     if i > n:
#         return
#     print(i)
#     print_numbers(i + 1, n)

# print_numbers(1, 5)

# 4. Printing N to 1

# def printntimes(n):
#     if n == 0:
#         return None
#     else:
#         print(n), printntimes(n-1)

# printntimes(5)

# 5. Sum of first N numbers

# def sumnnos(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sumnnos(n-1)
    
# print(sumnnos(5))

# 6. Factorial of N numbers

# def nfact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * nfact(n-1)
    
# print(nfact(5))

# 7. Reverse an array

# function to print array
# def printArray(arr, n):
#     print("The reversed array is:- ")
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()


# def reverseArray(arr, start, end):
#     if start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         reverseArray(arr, start + 1, end - 1)


# # Driver Code
# if __name__ == "__main__":
#     arr = [5, 4, 3, 2, 1]
#     n = len(arr)
#     reverseArray(arr, 0, n - 1)
#     printArray(arr, n)

# 8. Fibonacci series

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(6))