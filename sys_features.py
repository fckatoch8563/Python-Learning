import sys

def main():
    print("Hello, World!")
    print("Python version:", sys.version)
    print("File path:", sys.argv[0])
    print("Platform:", sys.platform)
    print("Executable path:", sys.executable)
    #print("User name:", sys.argv[1]) # This will throw an error if no user name is provided
    if len(sys.argv) > 1:
        print("User name:", sys.argv[1])
    else:
        print("User name: [not provided]")

if __name__ == "__main__":
    main() 

'''
The sys module provides many useful features for interacting 
with the Python runtime and environment. 
Here are some commonly used attributes and functions:

* sys.argv: List of command-line arguments.
* sys.version: Python version string.
* sys.platform: Platform identifier (e.g., 'darwin', 'win32').
* sys.executable: Path to the Python interpreter.
* sys.path: List of directories Python searches for modules.
* sys.modules: Dictionary of loaded modules.
* sys.exit(): Exit the program.
* sys.maxsize: Maximum integer value.
* sys.stdin, sys.stdout, sys.stderr: Standard input/output/error streams.
* sys.getsizeof(obj): Get the size of an object in bytes.
* sys.flags: Interpreter flags.
* sys.byteorder: Byte order ('little' or 'big').
* sys.getdefaultencoding(): Default string encoding.

You can use dir(sys) to see all available attributes and methods. 
Let me know if you want examples for any of these!''' 