#!/usr/bin/python
#
# By @josephmisiti 2-18-2013
#

"""
	Filter credit cards statements from Chase.com. 
	
	Usage:
	
	./clean <command-separated-tags> [case-insensitive]
	
	Example usage:
	
	./clean.py attm <--- filters all of my  AT&T wireless charges
	./clean.py mcdonald <--- filter all of my purchases at McDonald's
	./clean.py amazon <---- filter all of my amazon purchases
	./clean.py amazon,sprint <---- filter all of my amazon + sprint purchases
	./clean.py mcdonald,horton <---- filter all of my McDonald's + Tim Hortons
	
	You get the point .... right ?
"""

import os,sys,glob,re

TRANSACTION_LINE_REGEX = re.compile('(^[0-9]{2}\/[0-9]{2}[\s])')

def convert_to_float(price):
	price = price.replace(",","")
	try:
		return float(price)
	except:
		pass
		
def is_transaction_line(line): 
	"""
		Figures out if a line in your statements is a CC transations or not. Tranactions
		have the format
		
		<Date> ... bunch of spaces ...<Description>... bunch of spaces ...<Amount>	
	"""
	return len(TRANSACTION_LINE_REGEX.findall(line.strip())) > 0 and line[0] != 'x'

def filter_by_tags(tags, info):
	"""
		If purchase info matches case-insenstive tag info, its a tag hit, and
		should be displayed.
	"""
	info_as_list = [ t.lower() for t in info ]
	info_as_string = " ".join(info_as_list)
	tag_hit = False
	for tag in tags:
		if tag in info_as_list or tag in info_as_string:
			tag_hit = True
			break
	return tag_hit

def clean(files, tags=[], args=[]):
	"""
		Parse all CC statements, filter by purcahse lines, filter by tags, help me itemize
	"""
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

				SEP = "|" if 'sort' in args else "\t"

				if len(tags) == 0:
					print date_of_tranaction + SEP + transaction_info + SEP + "%s" % convert_to_float(amount)
				else:						
					if filter_by_tags(tags, line.strip().split()[1:-1]):
						print date_of_tranaction + SEP + transaction_info + SEP + "%s" % convert_to_float(amount)
						total_cost += convert_to_float(amount)
						
	print "The total was ", total_cost
		
if __name__ == "__main__":
	if len(sys.argv) > 1:
		tags = [t for t in sys.argv[1:][0].strip().split(',') if len(t) > 0 ]
		clean(glob.glob("./pdfs/*.txt"),tags=tags, args=sys.argv)
	else:
		clean(glob.glob("./pdfs/*.txt"),tags=[], args=sys.argv)
		