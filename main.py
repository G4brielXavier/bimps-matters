from utils.funcs import inp_cmd
from utils.cmd import interpreter, print, update_matter
from utils.database.info import appBimps

update_matter()

print()

print(f'{appBimps.name} [black]v{appBimps.version}[/black]')
print(f'by {appBimps.creator}')
print()
print('For more informations in "[u]https://github.com/G4brielXavier/BIMPS[/u]"')
    
print()

while True:
    cmd = inp_cmd()
    interpreter(cmd)