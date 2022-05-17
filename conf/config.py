import os
import sys
import yaml


from conf.path_config import project_dir

ENV = 'dev'

config_file = os.path.join(project_dir, f'conf/config_{ENV}.yaml')

with open(config_file, encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

if sys.platform.startswith('win'):
    MySQLConfig = config['mysql']
else:
    MySQLConfig = config['mysql_unix']

TushareConfig = config['tushare']

