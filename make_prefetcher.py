#from xml.etree.ElementTree import Element, SubElement, dump, parse
import csv, sys, argparse
from collections import defaultdict

loglist = []
fdnumber = 0
index = 0
fdlist = {}

#open source.c
convertfile = open("prefetcher.c", 'w');

#open csvfile
csv_file = open("TestCase.input", "rb");

#read pointer of csv
reader = csv.reader(csv_file)
convertfile.write("#include <fcntl.h>\n");
convertfile.write("#include <unistd.h>\n");
convertfile.write("#include <sys/types.h>\n");
convertfile.write("\n\n");
convertfile.write("int main(void) { \n")

for row in reader:
	#print row
	cells = list(row)

	if len(cells) != 0:
		loglist.append(cells)
	
for i in loglist:
	print i
	
# part1. open

for i in loglist:

	cells = i
	if fdlist.has_key(cells[2]) == False :	
		convertfile.write("\n");
		convertfile.write("\tint fd"+ str(fdnumber) + " = open(\"" + cells[2] + "\", O_RDONLY);\n")
		convertfile.write("\tposix_fadvise(fd" + str(fdnumber) + ", " + str(cells[3]) + ", " + str(cells[4]) + ", POSIX_FADV_NOREUSE);\n" )
		fdlist[cells[2]] = fdnumber
		fdnumber = fdnumber + 1
	else :
		convertfile.write("\tposix_fadvise(fd" + str(fdlist[cells[2]]) + ", " + str(cells[3]) + ", " + str(cells[4]) + ", POSIX_FADV_NOREUSE);\n" )



# part2. close

convertfile.write("\n\n");
for fd in range(0, fdnumber) :
	convertfile.write("\tclose(fd" + str(fd) + ");\n");



convertfile.write("\n\treturn 0;\n")
convertfile.write("}")
