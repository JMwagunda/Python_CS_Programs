import random
from collections import Counter
from rich.console import Console
from rich.table import Table

# Simulate rolling a fair six-sided die 1000 times
rolls = [random.randint(1, 6) for _ in range(1000)]

# Count the occurrences of each face
frequency_counter = Counter(rolls)

# Calculate the percentage occurrence of each face
percentage_occurrence = {face: count / 1000 * 100 for face, count in frequency_counter.items()}

# Create a table
table = Table(title="Dice Roll Statistics")
table.add_column("Face", justify="center", style="cyan", no_wrap=True)
table.add_column("Frequency", justify="center", style="magenta", no_wrap=True)
table.add_column("Percentage", justify="center", style="green", no_wrap=True)

# Populate the table using if statements
if frequency_counter.get(1):
    table.add_row("1", str(frequency_counter[1]), f"{percentage_occurrence.get(1, 0):.2f}%")
if frequency_counter.get(2):
    table.add_row("2", str(frequency_counter[2]), f"{percentage_occurrence.get(2, 0):.2f}%")
if frequency_counter.get(3):
    table.add_row("3", str(frequency_counter[3]), f"{percentage_occurrence.get(3, 0):.2f}%")
if frequency_counter.get(4):
    table.add_row("4", str(frequency_counter[4]), f"{percentage_occurrence.get(4, 0):.2f}%")
if frequency_counter.get(5):
    table.add_row("5", str(frequency_counter[5]), f"{percentage_occurrence.get(5, 0):.2f}%")
if frequency_counter.get(6):
    table.add_row("6", str(frequency_counter[6]), f"{percentage_occurrence.get(6, 0):.2f}%")

# Print the table using rich
console = Console()
console.print(table)
