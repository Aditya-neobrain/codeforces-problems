# Problem 484: Kola
# Problem url: https://codeforces.com/problemsets/acmsguru/problem/99999/484
import random
import time
from rich import print

cell_options = ['..', '<<', '>>']
n, m = 20, 15

# Generate a random grid with Kola and last row being empty
grid = [[random.choice(cell_options) for _ in range(m)] for _ in range(n-1)]
grid.append(['..' for _ in range(m)])

kola_position = (random.randint(0, n-1), random.randint(0, m-1))
grid[kola_position[0]][kola_position[1]] = '🥤'

print(f"Grid Size: {n}x{m}")
for row in grid:
    print(' '.join(row))


while True:
    time.sleep(0.3) 
    print("[red]" + "[::]"*28 + "[/red]")

    for row in grid:
        print(' '.join(row))

    kola_row, kola_col = kola_position
    below_row = kola_row + 1

    # Check if we hit the bottom
    if below_row >= n:
        print("\n[bold green]🥤 Kola has fallen off the bottom of the grid! 🥤[/bold green]")
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
            print("\n[bold yellow]Kola is stuck against the right wall![/bold yellow]")
            break
        elif grid[below_row][kola_col + 1] == '<<':
            print("\n[bold red]Kola is stuck between opposing belts (>> <<)![/bold red]")
            break
        else:
            # Move diagonally down-right
            grid[kola_row][kola_col] = '[bold green]::[/bold green]'
            kola_position = (below_row, kola_col + 1)
            grid[below_row][kola_col + 1] = '🥤'

    elif cell_below == '<<':
        # Slide Left
        if kola_col - 1 < 0:
            print("\n[bold yellow]Kola is stuck against the left wall![/bold yellow]")
            break
        elif grid[below_row][kola_col - 1] == '>>':
            print("\n[bold red]Kola is stuck between opposing belts (>> <<)![/bold red]")
            break
        else:
            # Move diagonally down-left
            grid[kola_row][kola_col] = '[bold green]::[/bold green]'
            kola_position = (below_row, kola_col - 1)
            grid[below_row][kola_col - 1] = '🥤'