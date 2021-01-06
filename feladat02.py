def szokoev(ev: int) -> bool:
  return ev % 400 == 0 or ev % 4 == 0 and ev % 100 != 0

#1992 -> true
#2000 -> true
#2001 -> false
#2100 -> false

print('2. feladat: szökőév listázó')
a = int(input('Kérem az első évszámot: '))
b = int(input('Kérem a második évszámot: '))
k_ev = min(a, b)
b_ev = max(a, b)

szokoevek = []
for ev in range(k_ev, b_ev):
  if szokoev(ev): szokoevek.append(ev)

if len(szokoevek) > 0:
  print(f'szokőévek: {szokoevek}')
else:
  print('Nincs szökőév a megadott tartományban')