import numpy as np
import re
import os
import itertools
import sys, getopt
from subprocess import call
import subprocess
import json
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
from sklearn.model_selection import train_test_split
from shutil import copyfile

if __name__ == "__main__":
	pdfs = None
	mappings = None
	opts, args = getopt.getopt(sys.argv[1:],"hc:p:m:s:")
	split = 0.5
	
for opt, arg in opts:
	if opt == '-h':
		print ("-q pdf folder, -m mapping file -s test to train ratio [0-1]")
	elif opt in ("-p"):
        	pdfs = arg
	elif opt in ("-m"):
		mappings = arg
	elif opt in ("-s"):
		split = arg


mappingContent = json.load(open(mappings))

dir = "pdf_splits_" + str(split)
if not os.path.exists(dir):
	os.makedirs(dir)

for key in mappingContent:
	amount = len(mappingContent[key])
	splits = train_test_split(mappingContent[key], test_size = float(split))
	topic_dir = dir + "/" + key
	train = splits[0]
	test = splits[1]

	if not os.path.exists(topic_dir):
		os.makedirs(topic_dir)

	for trainingSamp in train:
		topic_dir_train = topic_dir + "/train"
		if not os.path.exists(topic_dir_train):
			os.makedirs(topic_dir_train)
		copyfile(trainingSamp[0], topic_dir_train + "/" + trainingSamp[1])

	for testingSamp in test:
		topic_dir_test = topic_dir + "/test"
		if not os.path.exists(topic_dir_test):
			os.makedirs(topic_dir_test)
		copyfile(testingSamp[0], topic_dir_test + "/" + testingSamp[1])
        			
	

