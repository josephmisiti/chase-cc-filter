#!/usr/bin/python

###
### clean up these fucking pdfs ...
###

import os,sys,glob,re

TRANSACTION_LINE_REGEX = re.compile('(^[0-9]{2}\/[0-9]{2}[\s])')

def convert_to_float(price):
	price = price.replace(",","")
	try:
		return float(price)
	except:
		#print "failed on ", price
		pass
		
def is_transaction_line(line): 
	"""
		Figures out if a line in your statements is a CC transations or not. Tranactions
		have the format
		
		<Date> 
		
	"""
	return len(TRANSACTION_LINE_REGEX.findall(line.strip())) > 0 and line[0] != 'x'

def filter_by_tags(tags, info):
	info_as_list = [ t.lower() for t in info ]
	info_as_string = " ".join(info_as_list)
	tag_hit = False
	for tag in tags:
		if tag in info_as_list or tag in info_as_string:
			tag_hit = True
			break

	return tag_hit

def clean(files, tags=[]):
	total_cost = 0.0
	for f in files:
		lines = open(f,'r').readlines()
		for line in lines:
			line = line.strip()
			if is_transaction_line(line):
				info_as_list = [ t.lower() for t in line.strip().split()[1:-1] ]
				date_of_tranaction = line.strip().split()[0]
				transaction_info  = " ".join(line.strip().split()[1:-1])
				amount			= line.strip().split()[len(line.strip().split())-1]
			
				if len(tags) == 0:
					print date_of_tranaction,transaction_info, convert_to_float(amount)
				else:						
					if filter_by_tags(tags, line.strip().split()[1:-1]):
						print date_of_tranaction,transaction_info, convert_to_float(amount)
						total_cost += convert_to_float(amount)
						
	print "The total was ", total_cost
		
if __name__ == "__main__":
	if len(sys.argv) > 1:
		tags = [t for t in sys.argv[1:][0].strip().split(',') if len(t) > 0 ]
		clean(glob.glob("./*.txt"),tags=tags)
	else:
		clean(glob.glob("./*.txt"),tags=[])
		