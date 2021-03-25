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


# 删除信息
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


# 修改信息
def update():
    show()
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding=encode) as file:
            student_old = file.readlines()
    else:
        return
    student_id = input('请输入要修改的学生ID:')
    with open(fileName, 'w', encoding=encode) as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改他的相关信息')
                try:
                    d['name'] = input('请输入姓名：')
                    d['english'] = int(input('请输入英语成绩：'))
                    d['python'] = int(input('请输入Python成绩：'))
                    d['java'] = int(input('请输入Java成绩：'))
                except:
                    print('您的输入有误请重新输入')
                wfile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d)+'\n')
        answer = input('是否继续修改其他学生的信息y/n')
        if answer == 'y':
            update()


# 显示
def show():
    pass
