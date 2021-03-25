# -*- coding: utf-8 -*- 
# @Time : 2021/3/25 9:51 
# @Author : wyt
# @Description:学生信息管理系统
# @File : StudentSys.py
# 主函数
import OperateFile


def main():
    while True:
        choice = int(input('请选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('你确定要退出系统吗？(y/n):')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


# 菜单函数
def menu():
    print('****************************学生信息管理系统**********************************')
    print('-------------------------------功能菜单--------------------------------------')
    print('\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t\t0.退出')
    print('---------------------------------------------------------------------------')


# 新增
def insert():
    student_list = []
    while True:
        id = input('请输入ID(如1001)')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 保存学生信息
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加学生信息？(y/n)')
        if answer == 'y':
            continue
        else:
            break
    OperateFile.save(student_list)


# 查询
def search():
    pass


# 删除
def delete():
    while True:
        student_id = input('请输入要删除学生的ID:')
        if student_id != '':
            flag = OperateFile.delete(student_id)
            if not flag:
                break
            show()
            answer = input('是否继续删除?y/n')
            if answer == 'y':
                continue
            else:
                break


# 修改
def modify():
    pass


# 排序
def sort():
    pass


# 统计
def total():
    pass


# 显示
def show():
    pass


if __name__ == '__main__':
    main()
