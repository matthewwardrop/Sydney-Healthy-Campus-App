#!/usr/bin/python

print "Content-Type: text/plain;\r\n\r\n"

import simplejson as json
import sys,traceback

import cgitb
cgitb.enable()

# Import modules for CGI handling 
import cgi
 
 # Create instance of FieldStorage 
form = cgi.FieldStorage() 

mode = form.getvalue("mode")
if mode is None:
	mode = "module"

final_output = ""

def fieldStorageToDictionary(fs):
    mydict = {}
    for k in fs.keys():
        mydict[k] = fs.getvalue(k)
    return mydict

if mode == "module" or mode is None:
	module = form.getvalue("module")
	if module is None:
		module = "food"
	
	try:
		from helpers.module import AbstractModule
		moduleHandler = AbstractModule.getModule(module)
		moduleInfo = moduleHandler.render(form)
		moduleInfo['query'] = fieldStorageToDictionary(form)
		final_output = json.dumps(moduleInfo,ensure_ascii=True)
	except Exception, e:
		final_output = json.dumps(
			{
				"header": True,
				"menubar": True,
				"title": "System Error",
				"toolbar": ["stack"],
				"content": ["webview",{"html":"<h1>System Error:</h1> <br />" + e.message + "<br/><pre>" + traceback.format_exc() + "</pre>"}],
			}
		)
		
elif mode == 'menuitems':
	from modules import MODULE_INDEX
	
	module_descs = []
	for module,desc in MODULE_INDEX:
		module_descs.append( [desc.get("label",module).capitalize(),desc.get("icon",module),module] )
		
	final_output = json.dumps(module_descs)
elif mode == 'modules':
	from modules import MODULE_INDEX
	final_output = json.dumps(MODULE_INDEX)

if form.getvalue('callback'):
	print "%s(%s)" % (form.getvalue('callback'),final_output)
else:
	print final_output
