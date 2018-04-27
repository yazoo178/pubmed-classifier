import numpy as np
import matplotlib
import re
import os
import itertools
import sys, getopt
from subprocess import call
import subprocess


def readQrel(qrel, limit = 10):
	ids = {}
	file = open(qrel, "r")
	for line in file:
		tabbed = re.split('\s+', line)
		if '0' in tabbed[3].rstrip().strip():
			if tabbed[0] not in ids:
				ids[tabbed[0]] = []
			if len(ids[tabbed[0]]) < limit:
				ids[tabbed[0]].append(tabbed[2])

	return ids


def execute(ids):
	scripts = open("runners_all.sh", "w")
	for key in ids:
		runner = "sudo ruby pubmedid2pdf.rb "
		for document in ids[key]:
			runner = runner + document + ","
		runner = runner[:-1]
		scripts.write(runner + "\n")
	scripts.close()
	
	
		


opts, args = getopt.getopt(sys.argv[1:],"hc:q:")
qrel = None

for opt, arg in opts:
    if opt == '-h':
        print ("-q qrel file")
    elif opt in ("-q"):
	qrel = arg

ids = readQrel(qrel, 30)
execute(ids)


