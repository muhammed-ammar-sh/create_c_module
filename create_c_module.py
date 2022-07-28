import os
import sys

def generate_module(dir : str, module_name: str):
	module_name = module_name.lower()
	inc_guard_def = module_name.upper() + "_H"
	
	#.h file
	h_file_name = module_name + ".h"
	h_file = open(dir + "\\" + h_file_name, "w")
	h_file.write("#ifndef " + inc_guard_def + "\n" +
	             "#define " + inc_guard_def + "\n" + 
				 "\n" +
				 "\n" +
	             "#endif\n")
	h_file.close()

	#.c file
	c_file_name = module_name + ".c"
	c_file = open(dir + "\\" + c_file_name, "w")
	c_file.write("#include \""+ h_file_name  +"\"\n")
	c_file.close()



if __name__ == "__main__":
	cwd = os.getcwd()
	module_name = sys.argv[1]	## TODO: Check if the given name is valid ??
	generate_module(cwd, module_name)