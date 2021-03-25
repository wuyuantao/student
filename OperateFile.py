# -*- coding: utf-8 -*- 
# @Time : 2021/3/25 10:27 
# @Author : wyt
# @Description:进行文件的操作
# @File : OperateFile.py
import os

fileName = 'students.txt'
encode = 'utf-8'


# 保存信息
def save(lst):
    try:
        std_txt = open(fileName, 'a', encoding=encode)
    except:
        std_txt = open(fileName, 'w', encoding=encode)
    for student in lst:
        std_txt.write(str(student) + '\n')
    std_txt.close()


def delete(student_id):
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding=encode) as file:
            student_old = file.readlines()
    else:
        student_old = []
    flag = False
    if student_old:
        with open(fileName, 'w', encoding=encode) as wfile:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] != student_id:
                    wfile.write(str(d) + '\n')
                else:
                    flag = True
            if flag:
                print(f'id为{student_id}的学生信息已经被删除了')
            else:
                print(f'没有找到{student_id}的学生信息')
        return True
    else:
        print('无学生信息')
        return False
