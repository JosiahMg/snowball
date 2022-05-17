import os

"""-----------------------项目根路径---------------------------"""
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""-----------------------日志路径---------------------------"""
log_dir = os.path.join(project_dir, 'logs')

"""-----------------------资源路径---------------------------"""
resource_dir = os.path.join(project_dir, 'resource')
origin_data = os.path.join(resource_dir, 'data_qa.csv')


"""-----------------------结果输出路径---------------------------"""
outputs_dir = os.path.join(project_dir, 'outputs')
data_dir = os.path.join(outputs_dir, 'data')