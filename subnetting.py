from sys import argv

def subnet(networks):
	if networks == 0:
		return []

	hbit = 256//networks
	prefix = "192.168.1."
	ranges = []

	for i in range(networks):
		first = prefix + str(hbit * i)
		second = prefix + str((hbit * (i+1)) - 1)
		if i == networks - 1:
			second = prefix + '255'
		ranges.append((first,second))
	return ranges

if len(argv) > 1:
	print(subnet(int(argv[1])))
