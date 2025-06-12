playstation = 3200000
marzo =0.8
tioRico = 0.2
hugo = 0.5
Paco = 0.17
luis = 1 - ( tioRico+hugo+Paco)

cFebrero = playstation * marzo 

fTioRico = cFebrero * tioRico
fHugo = cFebrero * hugo
fpaco = cFebrero * Paco
fluis = cFebrero * luis

pTioRico = playstation * tioRico
pHugo = playstation * hugo
pPaco = playstation * Paco
pLuis = playstation * luis

regaloTio = playstation - 1500000

regaloHugo = regaloTio * hugo
regaloPaco = regaloTio * Paco
regaloLuis = regaloTio * luis

print ("la consola en febrero vale:", cFebrero)
print ("en febrero el tiorico pone:", fTioRico, "\n","hugo pone:", fHugo, "\n","paco pone:",fpaco, "\n","luis pone:", fluis)
print ("en marzo el tiorico pone:", pTioRico, "\n","hugo pone:", pHugo, "\n","paco pone:",pPaco, "\n","luis pone:", pLuis)
print ("si el tio rico les dara 1.500.000, los sobrinos deben poner","\n","hugo debe poner:",pHugo,"\n","paco debe poner fpaco", "\n","luis debe poner",pLuis)
