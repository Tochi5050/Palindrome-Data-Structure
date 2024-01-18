def isPalindrome(string):
  even = len(string) % 2


  if even == 0:
    return isPalindromeEven(string)
  if even > 0:
    return isPalindromeOdd(string)

def isPalindromeEven(string):
  array = list(string)
  midIdx = (len(array) - 1) // 2
  nextIdx = midIdx + 1

  while midIdx >= 0 and nextIdx <= len(array) - 1:
    if array[midIdx] == array[nextIdx]:
      midIdx -= 1
      nextIdx += 1
    else:
      return False
  return True

def isPalindromeOdd(string):
  array = list(string)
  midIdx = (len(array) - 1) // 2
  nextIdx = midIdx + 1
  prevIdx = midIdx - 1

  while prevIdx >= 0 and nextIdx <= len(array) - 1:
    if array[prevIdx] == array[nextIdx]:
      prevIdx -= 1
      nextIdx += 1
    else:
        return False
    return True

string = 'abfcba'
print(isPalindrome(string))

