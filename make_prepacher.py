from xml.etree.ElementTree import Element, SubElement, dump, parse


convertfile = open("prepacher.c", 'w');
tree = parse("output.xml")
root = tree.getroot()

convertfile.write("int main(void) { \n")

for element in root.findall("content"):
	fd = element.findtext("fd")
	where = element.findtext("where")
	start = element.findtext("start")
	end = element.findtext("end")
	convertfile.write("\tposix_fadvise(" + fd +"," + start + "," + end +"0 );\n") 
 

convertfile.write("\treturn 0;\n")
convertfile.write("}")

