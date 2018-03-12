from IPython.core.magic import Magics, magics_class, cell_magic
import sys

@magics_class
class WriteFileRun(Magics):
	
	@cell_magic
	def writefile_run(self, line, cell):
		"""
		
		"""

		args = line.strip().split(" ")
		args = [a for a in args if len(a)>0]
		if len(args)==0:
			sys.stderr.write("UsageError: the filename is a required argument")
			return

		
		filename = args[0]

		append = '-a' in args
		run = '-dr' not in args

		
		mode = 'a' if append else 'w'

		with open(filename, mode) as f:
			f.write(cell)
		
		if run:
			self.shell.run_cell(cell)

		print("Filename: "+str(filename))
		print("Append: "+str(append))
		print("Run: "+str(run))
		

try:
	ip = get_ipython()
	ip.register_magics(WriteFileRun)
except NameError:
	print('Not in IPython, this magic will have no effect')
