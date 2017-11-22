TARGET = int(input().split()[0])
nlist = sorted([int(n) for n in input().split()]) #

def kfac(state, nlist):
  curr = int(state.split()[-1])
  print(state)
  if not nlist and curr != TARGET:
    return -1

  for index, n in enumerate(nlist):

    if curr * n == TARGET:
      return state + ' ' + str(curr * n)
      # if too big try next
    elif curr * n > TARGET:
      # skip if too big
      return kfac(state, nlist[index+1:])
    else:
      # try multiplying by same factor
      return kfac(state + ' ' + str(curr), nlist)


    # elif curr * n > TARGET:
    #   # skip if too big
    #   return kfac(state, nlist[index+1:])
    # else:
    #   # we added, but should skip if ends w/o reaching target
    #   r = kfac(state + ' ' + str(curr * n), nlist[index+1:])

    #   return kfac(state, nlist[index+1:])


    # elif curr * n < TARGET:
    #   # add and keep on going
    #   return kfac(state + ' ' + str(curr * n), nlist[index+1:])
    # # add case for skipping? need to know other state of this ^
    # else:
    #   # skip
    #   return kfac(state, nlist[index+1:])

  # where do we return -1
  # get best answer lexicographically

kfac('1', nlist)
