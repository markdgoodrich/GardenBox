#Problem 112
#Bouncy numbers

def isBouncy(n):
	n = str(n)
	if all(n[i] <= n[i+1] for i in range(len(n)-1)):
		return "Increasing"
	if all(n[i] >= n[i+1] for i in range(len(n)-1)):
		return "Decreasing"
	else:
		return "Bouncy"
counter = 0
for a in range(1,10000000):
	if isBouncy(a) == "Bouncy":
		counter += 1
		
	percent = float(counter)/float(a)
	if percent >= .99:
		print a
		break

