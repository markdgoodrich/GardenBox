#check 1/p where p is a prime

p = [True] * (10**3)			#edit number here i suppose
p[0] = False
p[1] = False

for i in range(2, len(p)):
	if p[i]:
		j = i**2
		while j < len(p):
			p[j] = False
			j += i


primes = []
for n in range(len(p)):
	if p[n]:
		primes.append(n)
#now we have array of primes

print len(primes)		#168 primes




max = 0

#must find number n of cycles
# if n = p-1, we have our prime p


for p in primes:
	n=1
	while (10**n - 1) % p != 0 and n < p:  #Fermat's Little Theorem
		n +=1		#increment n
	if n == p-1:
		print p

