# Create C Module
Python script to generate a C module from a hard-coded template

## What Does This Script Do?
This script accepts an argument from the CLI (command line interface) as a module name and uses it to generate a C module (a header file + a source file)

For example: if this script is called with "gpio driver" argument, the next files will be generated in the current working directory.
- **gpio_driver.h**  
`#ifndef GPIO_DRIVER_H`  
`#define GPIO_DRIVER_H`  
` `  
`#endif`  

- **gpio_driver.c**  
  `#include "gpio_driver.h"`  


## How I'm Using This Script?
1. First I defined a function to call this script from the CLI. 

   In Powershell it will be something like:  
   `function create_c_module {python D:\workspace\scripts\create_c_module.py $arg}`

   In Linux Bash it will be something like:  
   `create_c_module() {  
	python /home/user/workspace/scripts/create_c_module.py "$1"  
   }`  

2. Then each time I want to create a new module, I can call the script directly from the CLI using the function that I've created  
   `create_c_module "gpio driver"`
