#!/usr/bin/python
def displayPathtoPrincess(n, grid):
  r = []
  for i, row in enumerate(grid):
    for j, char in enumerate(row):
      if j == 'p':
        pl = i, j
      if j == 'm':
        bl = i, j
  vert = pl[0] - bl[0]
  hor = pl[1] - bl[1]
  r.extend(['DOWN'] * vert)
  r.extend(['UP'] * -vert)
  r.extend(['RIGHT'] * hor)
  r.extend(['LEFT'] * -hor)
  print('\n'.join(r))

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
