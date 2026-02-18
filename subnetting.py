from sys import argv

def subnet(networks):
	"""
	Create ranges of IPV4 addresses based on a number of networks.
	Appends those network ranges as a list of tuples, then returns that list of tuples.
	"""
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

