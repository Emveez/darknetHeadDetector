import random
import os
import subprocess
import sys


def split_data_set(image_dir, s):

	f_val = open("test.txt", 'w')
	f_train = open("train.txt", 'w')
	
	path, dirs, files = next(os.walk(image_dir))
	data_size = len(files)

	ind = 0
	data_test_size = int(s * data_size)
	test_array = random.sample(range(data_size), k=data_test_size)
	n = len(os.listdir(image_dir))

	for f in os.listdir(image_dir):

		if(f.split(".")[1] == "jpg"):
			ind += 1
			
			if ind in test_array:
				f_val.write(image_dir+'/'+f+'\n')
			else:
				f_train.write(image_dir+'/'+f+'\n')

			print "Iter:{}/{}".format(ind, n)

	f_val.close()
	f_train.close()


def main():

	testShare = 0.1

	pwd = os.getcwd()

	p = pwd + "/JPEGImages"
	split_data_set(p, testShare)

if __name__ == '__main__':
	main()
