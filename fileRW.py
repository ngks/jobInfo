from pathlib import Path

p = Path('.')
print(list(p.glob('**/*.py')))

q = p / 'craw' / 'text.py'
with q.open() as f: 
    print(f.readline())