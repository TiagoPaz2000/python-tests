n1 = int(input('Digite o numero para saber sua tabuada: '))
indexWhile = 1
print('=' * 15)

while (indexWhile <= 10):
  print('{} X {:2} = {}'.format(n1, indexWhile, n1 * indexWhile))
  indexWhile += 1

print('=' * 15)