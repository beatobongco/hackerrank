i = input().split()
my_str = i[0]
times = int(i[1])

def recur(my_str):
  if len(my_str) == 1:
    return my_str

  return recur(str(sum([int(s) for s in my_str])))

stored = recur(my_str)

print(recur(stored * times))
