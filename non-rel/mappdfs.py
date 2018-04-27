import numpy as np
import matplotlib
import re
import os
import itertools
import sys, getopt
from subprocess import call
import subprocess
import json

def readQrel(qrel):
	ids = {}
	file = open(qrel, "r")
	for line in file:
		tabbed = re.split('\s+', line)
		if '0' in tabbed[3].rstrip().strip():
			if tabbed[0] not in ids:
				ids[tabbed[0]] = []
			ids[tabbed[0]].append(tabbed[2])

	return ids


def map(ids):

	mappings = {}
	for filename in os.listdir("pdf"):
		document = filename.split(".")[0]
		for key in ids:
			if document in ids[key]:
				if key not in mappings:
					mappings[key] = []
				mappings[key].append(["pdf/" + filename, document])

	
	with open('output_mappings.json', 'w') as file:
     		file.write(json.dumps(mappings, indent=4)) # use `json.loads` to do the reverse

	
	
		


opts, args = getopt.getopt(sys.argv[1:],"hc:q:")
qrel = None

for opt, arg in opts:
	if opt == '-h':
		print ("-q qrel file")
	elif opt in ("-q"):
		qrel = arg

ids = readQrel(qrel)
map(ids)


