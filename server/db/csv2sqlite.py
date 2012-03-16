# -*- coding: utf-8 -*-
import csv,sqlite3,re,json

f = open("RevisedDatabase.csv","Ur")
reader = csv.reader(f)

supertitles=reader.next()
titles = reader.next()

fields = supertitles[:supertitles.index("Average quantity per serving")]
fields.extend(titles[supertitles.index("Average quantity per serving"):supertitles.index("Average quantity per 100g")])

fields = map(lambda x: x.replace("(","").replace(")","").lower().strip().replace(" ","_"),fields)

print fields

values = []

try:
	while 1:
		valueSet=map(lambda x: unicode(x,"UTF-8"),reader.next())
		if valueSet == ['']*(len(valueSet)):
			continue
		if valueSet[0] == "":
			valueSet[0] = values[-1][0]
		values.append(map(unicode,valueSet[:supertitles.index("Average quantity per 100g")]))
except Exception, e:
	print e


def output_db():
	connection = sqlite3.connect("database.sqlite")

	c = connection.cursor()

	def getFieldType(field):
		if fields.index(field) >= supertitles.index("Average quantity per serving"):
			return "REAL"
		return "TEXT"

	sqlite_fields = map(lambda x: "%s %s" % (x,getFieldType(x)),fields)

	c.execute('''CREATE TABLE IF NOT EXISTS `foods` (%s)''' % ','.join(sqlite_fields))

	for valueSet in values:
		print '''INSERT INTO `foods` VALUES ('%s')''' % '\',\''.join(valueSet)
		c.execute('''INSERT INTO `foods` VALUES (%s)''' % ','.join(['?']*len(valueSet)),valueSet )

	connection.commit()
	c.close()

output_db()

def output_json():
	f = open('json.js','w')
	
	output = []
	
	for valueSet in values:
		d = {}
		for i,value in enumerate(valueSet):
			if (value):
				d[fields[i]] = value
		output.append(d)

	json.dump(output,f)
	f.close()

output_json()
