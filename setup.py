from cx_Freeze import setup, Executable

base = None    



executables = [Executable("main.py", base=base)]



# include all packages imported into the program here ex ["idna", "pygame", "os"]
packages = ["idna", "pygame", "sys"]  


options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Vault_map",
    options = options,
    version = "0.1",
    description = 'track rooms in Vault Hunters',
    executables = executables
)