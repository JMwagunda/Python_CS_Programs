from random import random
from tabulate import tabulate
from rich.console import Console
from rich.table import Table

console = Console()

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0

for i in range(1, 1001):
    number = random()

    if number >= 0 and number < (1 / 6):
        counter1 += 1

    elif number >= 1 / 6 and number < 2 / 6:
        counter2 += 1

    elif number >= 2 / 6 and number < 3 / 6:
        counter3 += 1

    elif number >= 3 / 6 and number < 4 / 6:
        counter4 += 1

    elif number >= 4 / 6 and number < 5 / 6:
        counter5 += 1

    elif number >= 5 / 6 and number < 6 / 6:
        counter6 += 1

percent_1 = round(counter1 * 0.1, 1)
percent_2 = round(counter2 * 0.1, 1)
percent_3 = round(counter3 * 0.1, 1)
percent_4 = round(counter4 * 0.1, 1)
percent_5 = round(counter5 * 0.1, 1)
percent_6 = round(counter6 * 0.1, 1)

total_counter = counter1 + counter2 + counter3 + counter4 + counter5 + counter6
total_percentage = round((percent_1 + percent_2 + percent_3 + percent_4 + percent_5 + percent_6), 1)

table = Table(title="Dice Roll Statistics")
table.add_column("Face", style="cyan")
table.add_column("Frequency", style="magenta")
table.add_column("Percentage (%)", style="green")

table.add_row("1", str(counter1), str(percent_1))
table.add_row("2", str(counter2), str(percent_2))
table.add_row("3", str(counter3), str(percent_3))
table.add_row("4", str(counter4), str(percent_4))
table.add_row("5", str(counter5), str(percent_5))
table.add_row("6", str(counter6), str(percent_6))
table.add_row("Total", str(total_counter), str(total_percentage))

console.print(table)
