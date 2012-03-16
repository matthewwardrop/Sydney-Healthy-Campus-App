from helpers.module import AbstractModule
import sqlite3,sys

class Module(AbstractModule):
	
	def render(self,form):
		
		years = {}
		for year in xrange(1940,2013):
			years[year] = year;
		
		return	{
			"header":True,
			"menubar": True,
			"toolbar": ["stack"],
			#"actions": ["search"],
			"title": "Profile",
			"layout": {"user":True},
			"content": ["list",{"class":"profile","list":[
				'Weight (kg):',
				['edit',{"value":"%(pref:weight)s","onchange":['pref_input',{'key':'weight'}]}],
				'Year of Birth:',
				['select',{"options":years,"selected":"%(pref:yob)s","onchange":['pref_input',{'key':'yob'}]}],
				'Gender:',
				['select',{"options":{"Male":"male","Female":"female"},"selected":"%(pref:gender)s","onchange":['pref_input',{'key':'gender'}]}],
				'Activity Level:',
				['select',{"options":{"Sedentary":1.4,"Low Active":1.7,"Active":1.8,"Very Active":2},"selected":"%(pref:activity)s","onchange":['pref_input',{'key':'activity'}]}]
			]}]
		}
