"""
有关文件的相关操作
"""
import os
import zipfile
from pandas.io.excel import ExcelWriter
import pandas as pd


def data_exists(dir_name):
    """
    判断文件夹下是否存在文件或文件夹  存在返回True
    :param dir_name: 文件夹路径
    :return:
    """
    if os.path.exists(dir_name):
        list_dirs = os.listdir(dir_name)
        if list_dirs:
            return True
    return False


def zip_fold(folder_name, zip_name):
    """
    压缩文件为zip格式
    :param folder_name: 指定被压缩的文件夹
    :param zip_name: 指定存放的路径和文件名
    :return:
    """
    z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(folder_name):
        fpath = dirpath.replace(folder_name, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


def csv2excel(folder_name, excel_path):
    """
    给定文件夹，将文件夹下的所有csv文件转成一个excel文件  excel文件的sheet name对于csv的文件名
    :param folder_name: 需要转的文件夹下的文件
    :param excel_path: 存放excel文件的路径
    :return:
    """
    with ExcelWriter(excel_path, mode='w') as writer:
        for dirpath, dirnames, filenames in os.walk(folder_name):
            for filename in filenames:
                if filename.endswith('.csv'):
                    file_path = os.path.join(dirpath, filename)
                    pd.read_csv(file_path).to_excel(writer, sheet_name=os.path.splitext(filename)[0], index=False)

