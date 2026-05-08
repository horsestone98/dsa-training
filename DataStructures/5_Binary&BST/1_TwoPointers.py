# This notebook is created to study two pointers and its use. 

# Example 1: 2Sum with target value

def twosum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current > target:
            right -= 1
        elif current < target:
            left += 1
        else:
            return [left + 1, right + 1]

    return [-1, -1]

vals = [-1,2,2,3,0,7]
tg = -1

# print(twosum(vals, tg))


def checkpalindrome(charac):
    s = "".join(x.lower() for x in charac if x.isalnum())

    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True

a = "A man, a plan, a canal: Panama"
print(checkpalindrome(a))