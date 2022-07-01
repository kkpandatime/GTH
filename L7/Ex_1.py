'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
'''

from pathlib import Path
import os

def dirs_struct(dirs: dict, par_file=''):

    for k, v in dirs.items():
        p = Path(f'{par_file}/{k}')
        p.mkdir(parents=True, exist_ok=True)
        if isinstance(v, dict):
            dirs_struct(v, f'{par_file}/{k}')


project = {'my_project': {'settings': {'photo': ['None'],
                                       'docs': 'None'},
                          'mainapp': None,
                          'adminapp': None,
                          'authapp': None}}

directory = os.path.abspath(os.curdir)

dirs_struct(project, directory)