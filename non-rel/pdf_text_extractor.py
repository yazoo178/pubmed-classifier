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

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text




if __name__ == "__main__":
	pdf = None
	opts, args = getopt.getopt(sys.argv[1:],"hc:p:")
   
	for opt, arg in opts:
    		if opt == '-h':
        		print ("-q pdf file")
    		elif opt in ("-p"):
        		pdf = arg	
	

	text = convert_pdf_to_txt(pdf)
	print(text)
