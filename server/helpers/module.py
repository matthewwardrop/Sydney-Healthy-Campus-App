class AbstractModule(object):
	def __init__(self, args):
		pass
	
	@classmethod
	def getModule(cls,name):
		from modules import MODULE_DICT
		if name in MODULE_DICT:
			moduleClass = __import__("modules.%s"%MODULE_DICT[name].get('module',name),fromlist=['Module'])
		else:
			raise ValueError, "Module not found."
		return moduleClass.Module(MODULE_DICT[name].get('init',None))
	
	def render(self,form):
		return {}
