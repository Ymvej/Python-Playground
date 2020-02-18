from ex2 import *

cc1 = [10, 18, 14, 11, 12, 16, 8]
cc2 = [8, 7, 2, 4, 11, 10]
ef = [16, 17, 18, 14, 12, 15, 19]

r = 0

cc1 = moyenne(cc1)
cc2 = moyenne(cc2)
ef = moyenne (ef)

r = moyenneTotale(cc1,cc2,ef)

print(admission(r), mention(r), '(avec une moyenne de ', cc1,' en CC1, ',cc2,' en CC2, et ',ef,' aux évualuations finales.)')
