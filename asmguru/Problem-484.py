# Problem 484: Kola
# Problem url: https://codeforces.com/problemsets/acmsguru/problem/99999/484

import random
import time
from rich.live import Live
from rich.panel import Panel

cell_options = ['..', '<<', '>>']
n, m = 20, 15

# Generating a random grid with Kola and last row being empty
grid = [[random.choice(cell_options) for _ in range(m)] for _ in range(n-1)]
grid.append(['..' for _ in range(m)])

kola_position = (random.randint(0,n-2), random.randint(0, m-1))
grid[kola_position[0]][kola_position[1]] = '🥤'

def generate_frame(grid, status=""):
    content = "\n".join(' '.join(row) for row in grid)
    
    if status:
        content += f"\n\n{status}"
        
    return Panel(content, title=f"Kola Grid {n}x{m}", expand=False)

status_message = "[bold blue]Kola is falling...[/bold blue]"

with Live(generate_frame(grid, status_message), refresh_per_second=10) as live:
    while True:
        time.sleep(0.3) 
        
        kola_row, kola_col = kola_position
        below_row = kola_row + 1

        # Check if we hit the bottom
        if below_row >= n:
            status_message = "[bold green]🥤 Kola has fallen off the bottom of the grid! 🥤[/bold green]"
            live.update(generate_frame(grid, status_message))
            break

        # Look at the cell directly below the Kola
        cell_below = grid[below_row][kola_col]

        if cell_below == '..':
            # Fall straight down
            grid[kola_row][kola_col] = '[bold green]::[/bold green]'
            kola_position = (below_row, kola_col)
            grid[below_row][kola_col] = '🥤'

        elif cell_below == '>>':
            # Slide Right
            if kola_col + 1 >= m:
                status_message = "[bold yellow]Kola is stuck against the right wall![/bold yellow]"
                live.update(generate_frame(grid, status_message))
                break
            elif grid[below_row][kola_col + 1] == '<<':
                status_message = "[bold red]Kola is stuck between opposing belts (>> <<)![/bold red]"
                live.update(generate_frame(grid, status_message))
                break
            else:
                # Move diagonally down-right
                grid[kola_row][kola_col] = '[bold green]::[/bold green]'
                kola_position = (below_row, kola_col + 1)
                grid[below_row][kola_col + 1] = '🥤'

        elif cell_below == '<<':
            # Slide Left
            if kola_col - 1 < 0:
                status_message = "[bold yellow]Kola is stuck against the left wall![/bold yellow]"
                live.update(generate_frame(grid, status_message))
                break
            elif grid[below_row][kola_col - 1] == '>>':
                status_message = "[bold red]Kola is stuck between opposing belts (>> <<)![/bold red]"
                live.update(generate_frame(grid, status_message))
                break
            else:
                # Move diagonally down-left
                grid[kola_row][kola_col] = '[bold green]::[/bold green]'
                kola_position = (below_row, kola_col - 1)
                grid[below_row][kola_col - 1] = '🥤'

        # Update the live display with the new grid and status
        live.update(generate_frame(grid, status_message))