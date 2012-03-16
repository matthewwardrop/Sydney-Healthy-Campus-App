# This is the file in which the modules are declared and mapped.
# The keywords for each module are:
#	"label": The string to be used in the user interface (defaults to key name).
#	"icon": The icon to be used (name only) (defaults to key name, with uppercase first letter).
#	"settings": A list of dicts with keys ["key","type","description"]
#	"menu": A list of dictionaries, with keys: (defaults to [{}]: one icon with default settings)
#			"label": The label of the menu icon (default to module label)
#			"query": Query arguments to be sent to module constructor (defaults to None)
#			"icon": Defaults to module icon.
#			"category": Defaults to ""

MODULE_INDEX = [
		("profile", {"menu":[{"category":"Healthy Campus"}]}),
		("food", {"menu":[{"category":"Healthy Campus"}],"label":"Food Database"}),
	]
MODULE_DICT = {}
for name,desc in MODULE_INDEX:
	MODULE_DICT[name] = desc
	
# Each module returns a dictionary which can have any of the following keys:
# 	"header" (boolean): Whether header is shown (true)
#	"menubar" (boolean): Whether menubar is shown (true)
#	"toolbar" ( ["<type>", {opts}] ) : Type and options to toolbar (null)
#	"content" ( ["<type>", {opts}] ) : Type and options for main view (-)
#	"action": The actions available to this module. Currently just search. (list of strings).
