# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:40:30 2020

@author: Meaghan
"""

import csv
def __main__():
    course = input('Course: ')
    sem = input('Semester: ')
    crs_this_sem = input('Course Running: ')
    student_list = []
    with open(f'{sem}/rosters/{course}.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            build_classes(row, student_list,sem,course)
        for student in student_list:
            running(student, crs_this_sem)
        
class Student:
    def __init__(self, id_num, name, email):
        self.id_num=id_num
        self.name=name
        self.email=email
        self.com=[]
        self.ip={}
        
def build_classes(info, student_list, sem,cou):
    s = Student(info[0],info[1],info[2])
    with open(str(sem) + '/transcripts/' + str(s.id_num) + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0]+row[1] in ['ARCH463','ARCH464','ARCH563']:
                s.com.append(row[0]+row[1])
        student_list.append(s)

def running(student, crs_run):
    if student.com.count(crs_run) > 1:
        needs = [c for c in ['ARCH463','ARCH464','ARCH563'] if c not in student.com]
        print(student.name, ";", student.id_num, ";",needs)


__main__()