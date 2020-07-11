def rotations(t):
	""" Return list of rotations of input string t """ 
	tt = t * 2
	return [ tt[i:i+len(t)] for i in list(range(0, len(t))) ]


def bwm(t):
	""" Return lexicographically sorted list of t’s rotations (BWM) """
	return sorted(rotations(t))


def bwt_via_bwm(t):
	""" Given a string T, returns BWT(T) by way of the BWM """
	return ''.join(map(lambda x: x[-1], bwm(t)))


def main():
	sequence = input('Enter sequence: ')
	sequence += "$"
	final = bwt_via_bwm(sequence)
	print('Burrows-Wheeler Transform:\t{}'.format(final))


if __name__ == "__main__":
	main()
