def ps(x, i=1, n=2):
  count = 0
  while i ** n <= x:
    test = i ** n

    if test == x:
      count += 1
    else:
      count += ps(x - test, i + 1, n)

    i += 1

  return count


def count(x, n):
  nums = []
  total = 0
  extend = True
  count = 0
  while 1:
    if extend:
      if nums:
        num = nums[-1] + 1
      else:
        num = 1
      nums.append(num)
      total += num ** n
    else:
      if not nums:
        break
      last = nums[-1]
      nums[-1] += 1
      total += (last + 1) ** n - last ** n
      extend = True
    if total >= x:
      count += total == x
      total -= nums.pop() ** n
      extend = False
  return count

