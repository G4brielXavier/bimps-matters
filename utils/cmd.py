from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED

from rich import print, console

from pandas import read_json
from os import system
from time import sleep

from utils.help import commands
import json

console = Console()
matter_table = None

matters = 0 # control matters
limit_matter = 20 # limit of matters
current_bim = 4 # default '4'
favorite_matter = ''

# listAll - show table of all matters
def list_all():
    print()
    console.log(matter_table)
    print()

# listSpec - custom search
def list_spec():
    global limit_matter
    global current_bim
    
    matter_data = read_json('./utils/database/datas.json')
    
    print()
    matter_spec = input(' ~matter: ').upper()
    print()
    
    for _ in range(limit_matter):
        for matter, value in matter_data.items():
            if matter == matter_spec:
                
                print(f'Matter: [bold green]{matter_spec}[/bold green]')
                print()
                
                for i, v in enumerate(value):
                    print(f'[black]Bim {i+1}[/black]: [green]{v}[/green]' if v >= 6 else f'[black]Bim {i+1}[/black]: [red]{v}[/red]') 
                
                tot_value = sum(value) / current_bim
                status = ''
                
                if tot_value < 6:
                    status = '[bold red]bad[/bold red]'
                elif tot_value >= 6 and tot_value < 8:
                    status = '[bold green]good[/bold green]'
                elif tot_value >= 8:
                    status = '[bold yellow]nice[/bold yellow]'
                
                print()
                print(f'Status: {status}')
                print(f'Average: [green]{tot_value:.1f}[/green]' if tot_value >= 6 else f'AVERAGE: [red]{tot_value:.1f}[/red]')
                print()
        
                return
        
        print()
        print(f'[bold red]Error[/bold red] ~ The [u]{matter_spec}[/u] not found.')
        print()
        
        return
      
# updateTable - update the table of matters
def update_matter(status_filter=''):
    # global variables
    global limit_matter
    global matters
    global matter_table
    global current_bim
    global favorite_matter
    
    # building table
    matter_table = Table(header_style="magenta", box=ROUNDED)
    matter_table.add_column('Matters', style="dim")
    matter_table.add_column('Bim 1' if current_bim >= 1 else '[black]Bim 1[/black]', width=10)
    matter_table.add_column('Bim 2' if current_bim >= 2 else '[black]Bim 2[/black]', width=10)
    matter_table.add_column('Bim 3' if current_bim >= 3 else '[black]Bim 3[/black]', width=10)
    matter_table.add_column('Bim 4' if current_bim == 4 else '[black]Bim 4[/black]', width=10)
    matter_table.add_column('Status', width=15, justify="center")
    
    # matters
    matters = 0
    
    try:
        matter_data = read_json('./utils/database/datas.json')
    
        if matters < limit_matter:
            print()
            for matter, value in matter_data.items():
            
                tot_value = sum(value) / current_bim
                status = ''
                
                bad = tot_value < 6
                good = tot_value >= 6 and tot_value < 8
                nice = tot_value >= 8
                
                if status_filter == '':
                    if bad: status = '[bold red]bad[/bold red]'
                    elif good: status = '[bold green]good[/bold green]'
                    elif nice: status = '[bold yellow]nice[/bold yellow]'

                    matter_table.add_row(
                        matter, str(value[0]), str(value[1]), str(value[2]), str(value[3]), status
                    )
                
                if status_filter == 'bad' and bad:
                    matter_table.add_row(
                        matter, str(value[0]), str(value[1]), str(value[2]), str(value[3]), '[bold red]bad[/bold red]'
                    )                   
                    
                if status_filter == 'good' and good:
                    matter_table.add_row(
                        matter, str(value[0]), str(value[1]), str(value[2]), str(value[3]), '[bold green]good[/bold green]'
                    )
                    
                if status_filter == 'nice' and nice:
                    matter_table.add_row(
                        matter, str(value[0]), str(value[1]), str(value[2]), str(value[3]), '[bold yellow]nice[/bold yellow]'
                    )
                
                matters += 1
                
            with console.status('[green]Updating[/green]') as st:
            
                sleep(2)
                console.log('[bold green]Updated[/bold green]')  
                return
            
    except Exception as err:
        
        print()
        print(f'[bold red]Error[/bold red] ~ {err}')
        print()
        return 

# setPoint - set a point in matter
def set_point():
    
    try:
        print()
        set_edit = input('@: ')
        steps = set_edit.split(' ')

        matter = steps[0].upper()
        bim = int(steps[1])
        point = float(steps[2])
        
        with open('./utils/database/datas.json', 'r') as f:
            data = json.load(f)
        
        data[matter][bim] = point
            
        with open('./utils/database/datas.json', 'w') as f:
            json.dump(data, f)
            
        print()
        print(f'[bold green]Success[/bold green] ~ edited [u]{matter}[/u]')
        print()
        
        return
    
    except Exception as err:
        
        print()
        print(f'[bold red]Error[/bold red] ~ {err}')
        print()
        
        return

# setCurrentBim - set your current bim
def set_current_bim():
    global current_bim
    
    print()
    try:
        
        current_bim_edit = int(input(' @current: '))
        if current_bim_edit >= 1 or current_bim_edit <= 4:
        
            current_bim = current_bim_edit
            
            print()
            print(f'[bold green]Success[/bold green] ~ Current Bim is "{current_bim_edit}"')
            print()
            return
        
    except Exception as err:
        print()
        print(f'[bold red]Error[/bold red] ~ {err}')
        print()
        
# currentBim - view current bim
def view_current_bim():
    global current_bim
    
    print()
    print(f'[black]{current_bim}[/black]')
    print()
    return    
            
# help - view all commands of BIMPS
def help_view():
    print()
    
    for k, v in commands.items():
        print(f'[bold blue]{k}[/bold blue] : [black]{v}[/black]')
        print()
        
    return

# helpCmd - view a specifie command of BIMPS
def help_cmd():
    print()
    
    cmdSpec = input("@cmd: ")
    print()
    
    for k, v in commands.items():
        if k == cmdSpec:
            print(f'[bold blue]{k}[/bold blue] : [black]{v}[/black]')

    print() 
    return
        
# bestMatter - matter as the best status
def best_matter():
    global current_bim
    
    points_data = []
    matter_data = read_json('./utils/database/datas.json')
    
    for matter, points in matter_data.items():
        base = []
        
        base.append(sum(points) / current_bim)
        base.append(matter)
        points_data.append(base.copy())
        
        base.clear()
        
    matters = [v[1] for v in points_data]
    points = [v[0] for v in points_data]
    
    best_point = max(points)
    
    print()
    print(f'[bold green]{matters[points.index(best_point)]}[/bold green]: Average - {best_point:.1f} pts')
    print()
        
    return

# filterStatus - filter according to points
def filter_status():
    global current_bim
    
    print()
    status_spec = input('@status: ')
    
    if status_spec in ['nice', 'good', 'bad'] and not status_spec == '':
        update_matter(status_spec)
        return 
        
    print()
    print(f'[bold red]Error[/bold red] ~ Only "nice", "good" or "bad"')
    print()
    return 

# worseMatter
def worse_matter():
    global current_bim
    
    points_data = []
    matter_data = read_json('./utils/database/datas.json')
    
    for matter, points in matter_data.items():
        base = []
        
        base.append(sum(points) / current_bim)
        base.append(matter)
        points_data.append(base.copy())
        
        base.clear()
        
    matters = [v[1] for v in points_data]
    points = [v[0] for v in points_data]
    
    worse_point = min(points)
    
    print()
    print(f'[bold green]{matters[points.index(worse_point)]}[/bold green]: Average - {worse_point:.1f} pts')
    print()
        
    return
       
# global interpreter
def interpreter(cmd):
    match cmd:
        
        case 'listAll':
            list_all()
        
        case 'listSpec':
            list_spec()
        
        case 'updateTable':
            update_matter()
            
        case 'setPoint':
            set_point()
            
        case 'setCurrentBim':
            set_current_bim()
            
        case 'currentBim':
            view_current_bim()
        
        case 'help':
            help_view()
            
        case 'helpCmd':
            help_cmd()
            
        case 'bestMatter':
            best_matter()
            
        case 'filterStatus':
            filter_status()
        
        case 'worseMatter':
            worse_matter()
            
        case 'cls':
            system('cls')
            
        case 'clear':
            system('cls')
            
        
        
        case _:
            print()
            print(f'[bold red]Error[/bold red] ~ The [u]{cmd}[/u] not exist.')
            print()
