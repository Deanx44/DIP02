import numpy as np

a = np.array([[17, 24, 1, 8, 15],
              [23, 5, 7, 14, 16],
              [4, 6, 13, 20, 22],
              [10, 12, 19, 21, 3],
              [11, 18, 25, 2, 9]])

print('a=')
print(a)

b = int(input('Enter the row < size of Matrix: '))
c = int(input('Enter the column < size of matrix: '))
print('input(Element):')
print(a[b-1, c-1])

# 4 Point Neighbour
N4 = [a[b-2, c-1], a[b-1, c-2], a[b-1, c], a[b, c-1]]
print('N4=')
print(N4)

# 8 Point Neighbour
N8 = [a[b-2, c-2], a[b-2, c-1], a[b-2, c], a[b-1, c-2], a[b-1, c], a[b, c-2], a[b, c-1], a[b, c]]
print('N8=')
print(N8)

# Diagonal Neighbour
ND = [a[b-2, c-2], a[b-2, c], a[b, c-2], a[b, c]]
print('ND=')
print(ND)