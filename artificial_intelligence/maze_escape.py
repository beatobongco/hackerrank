m = int(input())
grid = []
for i in range(0, 3):
  grid.append(input().strip())

if grid[1][2] == '#':
  if grid[0][1] == '#':
    print('LEFT')
  else:
    print('UP')
else:
  if grid[2][2] == '#':
    print('RIGHT')
  else:
    print('LEFT')
