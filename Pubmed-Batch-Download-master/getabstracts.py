import numpy as np
import re
import os
import itertools
import sys, getopt
from subprocess import call
import subprocess
from Bio.Entrez import efetch, read
from Bio import Entrez

def fetch_abstract(pmid):
    print(pmid)
    Entrez.email = 'wbriggs2@sheffield.ac.uk'	
    handle = efetch(db='pubmed', id=pmid, retmode='xml')
    
    xml_data = read(handle)
    return xml_data



def readQrel(qrel, limit = 10):
	ids = {}
	file = open(qrel, "r")
	for line in file:
		tabbed = re.split('\s+', line)
		if tabbed[0] not in ids:
			ids[tabbed[0]] = []
		if len(ids[tabbed[0]]) < limit:
			ids[tabbed[0]].append([tabbed[2], tabbed[3].rstrip().strip()])

	return ids


def execute(ids):
	for key in ids:
		for doc in ids[key]:
			content = fetch_abstract(doc[0])
			print(content['PubmedArticle'][0]['MedlineCitation']['Article']['ArticleTitle'])
			print(content['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract'])
			break
	
		break
		


opts, args = getopt.getopt(sys.argv[1:],"hc:q:")
qrel = None

for opt, arg in opts:
    if opt == '-h':
        print ("-q qrel file")
    elif opt in ("-q"):
        qrel = arg

ids = readQrel(qrel, 3000000)
execute(ids)


