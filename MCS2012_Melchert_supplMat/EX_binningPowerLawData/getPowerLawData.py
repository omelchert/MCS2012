from random import seed, random

## inversion method to obtain power law
## distributed pseudo random numbers
N=1000000
seed(0)
alpha=2.5
for i in range(N):
	print pow(1.-random() , -1./(alpha-1.)  )
