#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# author:"Zhang Shuyu"
#!/bin/bash
'''对指定路径中的json文件进行解析，生成相应的数据'''
import os
import natsort
labelme_json = "C:\DiskD\Anaconda3\envs\labelme\Scripts\labelme_json_to_dataset.exe" #labelme_json_to_dataset.exe 程序路径
file_path = "C:\\Users\\Lsk\\Desktop\\RGB_N\\matlab\\提取坐标\\myimitate"   # 处理文件所在路径
dir_info = os.listdir(file_path)
dir_info = natsort.natsorted(dir_info)
"""循环处理‘.json’文件"""
for file_name in dir_info:
    file_name = os.path.join(file_path + "\\" + file_name)
#    os.system('cd C:\\Users\\Lsk\\Desktop\\RGB_N\\matlab\\提取坐标\\myimitate2')
    os.system(labelme_json + " " + file_name)