class Epulet:
  def __init__(self, sor):
    self.nev = sor[0]
    self.varos = sor[1]
    self.orszag = sor[2]
    self.magassag = float(sor[3].replace(',', '.'))
    self.emelet = int(sor[4])
    self.ev = int(sor[5])

#3.1 feladat:
epuletek = []
for sor in open("legmagasabb.txt", encoding="UTF-8").read().splitlines()[1:]:
  epuletek.append(Epulet(sor.split(';')))

#3.2 feladat:
print(f'3.2 feladat: Épületek száma: {len(epuletek)} db')

#3.3 feladat:
sum = 0
for e in epuletek: sum += e.emelet
print(f'3.3 feladat: Emeletek összege: {sum}')

#3.4 feladat:
maxi = 0
for i in range(1, len(epuletek)):
  if epuletek[i].magassag > epuletek[maxi].magassag: maxi = i
print(f'\tNév: {epuletek[maxi].nev}')
print(f'\tVáros: {epuletek[maxi].varos}')
print(f'\tOrszág: {epuletek[maxi].orszag}')
print(f'\tMagasság: {epuletek[maxi].magassag}')
print(f'\tEmeletek száma: {epuletek[maxi].emelet}')
print(f'\tÉpítés éve: {epuletek[maxi].ev}')

#3.5 feladat:
i = 0
print('3.5 feladat:', end=" ")
while(i < len(epuletek)):
  if(epuletek[i].orszag == "Olaszország"): 
    print('Van olasz épület az adatok között!')
    break
  i += 1
else: print('Nincs olasz épület az adatok között!')