from helpers.module import AbstractModule
import sqlite3,sys

class Module(AbstractModule):
	
	def render(self,form):
		
		connection = sqlite3.connect(sys.path[0]+"/db/database.sqlite")
		c = connection.cursor()
		
		if form.getvalue("food"):
			food = form.getvalue("food")
			
			c.execute("SELECT * FROM `foods` WHERE `food_name` = ?",[u"%s" % food.decode('utf-8')])
			
			columns = map(lambda x: x[0],c.description)
			food = c.fetchone()
			
			template = """
			<div class='foodInfo'>
				%s
			</div>
			"""
			
			infoOrder = [
				#["food_name","name"],
				["vendor","vendor"],
				["ingredients","ingredients"],
				["energy_kj","detail","Energy", "<span class='progress' style='width: %%(percentEER:%(value)f)s%%;'></span> <span class='progress_text'>%(value).1f kJ (%%(percentEER:%(value)f)s %%RDI)</span>"],
				["protein_g","detail","Protein", "<span class='progress' style='width: %%(percentProtein:%(value)f)s%%;'></span> <span class='progress_text'>%(value).1f g (%%(percentProtein:%(value)f)s %%RDI)</span>"],
				["fat_g_total","detail","Total Fat", "<span class='progress' style='width: %%(percentTotalFat:%(value)f)s%%;'></span> <span class='progress_text'>%(value).1f g (%%(percentTotalFat:%(value)f)s %%RDI)</span>"],
				["saturated_fat_g","detail","Saturated Fat", "<span class='progress' style='width: %%(percentSatFat:%(value)f)s%%;'></span> <span class='progress_text'>%(value).1f g (%%(percentSatFat:%(value)f)s %%RDI)</span>"],
				["carbohydrate_g","detail","Carbohydrates", "<span class='progress' style='width: %%(percentCarbohydrates:%(value)f)s%%;'></span> <span class='progress_text'>%(value).1f g (%%(percentCarbohydrates:%(value)f)s %%RDI)</span>"],
				["sodium_mg","detail","Sodium", "<span class='progress' style='width: %%(percentSodium:%(value)f)s%%;'></span> <span class='progress_text'>%(value).1f mg (%%(percentSodium:%(value)f)s %%RDI)</span>"],
				["serving_size_g","serving"],
				["source","source"],
			]
			
			output = []
			for item in infoOrder:
				info = {
					'classname':item[1],
					'key':item[0],
					'value':food[columns.index(item[0])],
				}
				if not info['value']:
					continue
				if item[1] == "detail":
					if len(item) >2:
						info['key'] = item[2]
					if len(item) >3:
						info['value'] = item[3] % info
					output.append("<span class='%(classname)s'><span class='key'>%(key)s</span><span class='value'>%(value)s</span></span>" % (info) )
				else:
					output.append("<span class='%s'>%s</span>" % (item[1],food[columns.index(item[0])]) )
			
			'''output.append("<span class='subheader'>Other</span>");
			for i,column in enumerate(columns):
				if column not in map(lambda x: x[0],infoOrder):
					item = [column,"detail",column]
					if item[1] == "detail":
						output.append("<span class='%s'><span class='key'>%s</span><span class='value'>%s</span></span>" % (item[1],item[0],food[columns.index(item[0])]) )
					else:
						output.append("<span class='%s'>%s</span>" % (item[1],food[columns.index(column)]) )'''
			
			c.close()
			
			return	{
				"header":True,
				"menubar": True,
				"toolbar": ["stack"],
				#"actions": ["search"],
				"title": u"%s" % (food[columns.index("food_name")]),
				"content": ["webview",{"html": template % '\n'.join(output),"scroll":True}]
			}
			
		if form.getvalue("category"):
			category = form.getvalue("category")
			
			c.execute("SELECT `food_name` FROM `foods` WHERE `food_category` = ?",[u"%s" % category.decode("utf-8",'ignore')])
		
			foods = []
			for food in c:
				foods.append({
						"view": "template",
						"fields": {"label":u'%s' % (food[0])},
						"section": "Foods",
						"template":"test",
						"onclick": ["push",{'query':{'module':'food','food':u'%s' % (food[0])}}]
					})
			
			c.close()
			return	{
				"header":True,
				"menubar": True,
				"toolbar": ["stack"],
				#"actions": ["search"],
				"title": u"%s" % (category.decode('utf-8','ignore')),
				"content": ["list",{"list":foods,"templates":{'test':"%(label)s"},"scroll":True}]
			}
		else:
			c.execute("SELECT `food_category` FROM `foods` GROUP BY `food_category`")
		
			categories = []
			for category in c:
				categories.append({
						"view": "template",
						"fields": {	"label":u'%s' % (category[0]) },
						"section": "Categories",
						"template": "test",
						"onclick": ["push",{'query':{'module':'food','category':u'%s' % (category[0])}}]
					})
			
			c.close()
			return	{
				"header":True,
				"menubar": True,
				"toolbar": ["stack"],
				#"actions": ["search"],
				"title": "Food",
				"content": ["list",{"list":categories,"scroll":True,"templates":{'test':"%(label)s"}}]
			}
