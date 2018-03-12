from IPython.core.magic import Magics, magics_class, cell_magic


@magics_class
class WriteFileRun(Magics):
	
	@cell_magic
	def writefile_run(self, line, cell):
		pass


try:
	ip = get_ipython()
	ip.register_magics(WriteFileRun)
except NameError:
	log.debug('Not in IPython, this magic will have no effect')
