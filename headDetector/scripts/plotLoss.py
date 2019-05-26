import matplotlib.pyplot as plt
import numpy as np

def parseData(file):

	loss = []
	with open(file, 'r') as f:
		for line in f.readlines():
			if "avg" in line:
				loss.append(float(line.split(" ")[2]))

	return np.array(loss)


def main():

	f = 'train.log'

	avgLoss = parseData(f)
	idx = np.arange(avgLoss.size)

	n = 300

	p = plt.figure()
	plt.plot(idx, avgLoss)
	p.savefig("loss.png")






if __name__ == '__main__':
	main()