import os
from datetime import datetime

t = datetime.now().strftime("%Y-%m-%d_%H%M%S")
root_path = os.getcwd()
print(root_path)
path = os.path.join(root_path,f'{t}{os.sep}')
print(path)