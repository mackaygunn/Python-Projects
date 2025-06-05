amount = int(input('amount: '))

coinslist = [1, 2, 5, 10, 20, 50, 100]
coinslist.sort(reverse= True)

coinsused = []

for coin in coinslist:
   while amount >= coin:
    amount = amount - coin
    coinsused.append(coin)

print(coinsused)
print('total coins used', len(coinsused))
