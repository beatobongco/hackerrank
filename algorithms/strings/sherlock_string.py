#!/bin/python3

import sys
from collections import Counter

def isValid(s):
  v = Counter(s)

  def isSameFreq(v):
    if len(set(v.values())) == 1:
      return True

  def testOdd(v):
    # must be 2 since we're looking for just one off
    common_val = Counter(v.values()).most_common(1)[0][0] # get most common
    for i in v:
      if v[i] == common_val:
        pass
      elif v[i] == 1:
        v.pop(i)
        return isSameFreq(v)
      elif v[i] == common_val + 1:
        v[i] -= 1
        return isSameFreq(v)
      else:
        return False
    return True

  if isSameFreq(v):
    return "YES"
  elif testOdd(v):
    return "YES"

  return "NO"

s = input().strip()
result = isValid(s)
print(result)
