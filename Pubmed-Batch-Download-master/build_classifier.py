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
from pdf_text_extractor import convert_pdf_to_txt



def processpdf(pdf):
	return pdf

if __name__ == "__main__":
	pdfDir = None
	opts, args = getopt.getopt(sys.argv[1:],"hc:p:")
	train = []
	test = []
	
	for opt, arg in opts:
		if opt == '-h':
			print ("-p pdf dir, expected to contain a test and train folder")

		elif opt in ("-p"):
			pdfDir = arg	

	for topic in os.listdir(pdfDir):
		for dataFolder in os.listdir(pdfDir + "/" + topic):
			if dataFolder == "train":
				for file in os.listdir(pdfDir + "/" + topic + "/" + dataFolder):
					text = convert_pdf_to_txt(pdfDir + "/" + topic + "/" + dataFolder + "/" + file)
					pdf = processpdf(pdf)
					train.append(pdf)
		
			elif dataFolder == "test":
				for file in os.listdir(pdfDir + "/" + topic + "/" + dataFolder):
					current_study = pdfDir + "/" + topic + "/" + dataFolder + "/" + file
					print(current_study)
					text = convert_pdf_to_txt(current_study)
					pdf = processpdf(text)
					test.append(pdf)


	print(train)
	print(test)




			
