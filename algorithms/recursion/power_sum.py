x = input() # target sum
n = input() # power

def powersum(x, n):
  # generate initial list
  r = [1]
  tmp = 1
  s = 1
  while s < x:
    tmp += 1
    s = tmp ** n
    r.append(s)

  def test_list(currlist):
    currsum = 0
    for j in currlist:
      currsum += j
      if currsum == x:
        return True
      if currsum > x:
        return False

  count = 0
  while r:
    if test_list(r):
      count += 1
    r.pop(0)

  return count
