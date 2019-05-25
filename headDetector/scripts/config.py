import os



def main():
	pwd = os.getcwd()
	c = open("./config/headData.data", 'w')

	classes = "classes=1\n"
	train = "train  = " + pwd + "/train.txt\n"
	valid = "valid  = " + pwd + "/test.txt\n"
	names = "names = " + pwd + "/config/" + "classes.names\n"
	backup = "backup = " + pwd + "/checkpointWeights\n"

	c.write(classes)
	c.write(train)
	c.write(valid)
	c.write(names)
	c.write(backup)
	c.close()


if __name__ == '__main__':
	main()