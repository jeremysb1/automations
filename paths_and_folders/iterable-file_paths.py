from pathlib import Path

path = Path.home() / 'Desktop' / 'automations'

for item in path.iterdir():
    print(item)