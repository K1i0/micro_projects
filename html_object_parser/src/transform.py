#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import datetime
import transform as tf
import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import ttk
# # Заменить значения в кавычках (day, month, year), если нужно
def prepare_data(textWindow, sfile):
    current_time = datetime.datetime.now()

    day = current_time.day;
    month = current_time.month;
    year = current_time.year;

    # remove tags
    with open("data/inter.txt", "w", encoding="utf-8") as ifile:
        data = sfile.read()
        data = re.sub(r'<.+?>', '\n', data)
        data = data.replace('&nbsp;', '')
        ifile.write(data)
    # remove empty lines
    with open("data/inter.txt", "r", encoding="utf-8") as ifile, \
        open("data/dest.txt", "w", encoding="utf-8") as dfile:
        for line in ifile:
            if line.strip():
                dfile.write(line)
                textWindow.insert(tk.END, line)
    # json structure pattern
    part_1 = "{\"pr3\":\"true\",\"code\":\""
    part_1_1 = "\",\"dataNi\":"
    part_2 = ",\"fullname\":\""
    part_3 = "\",\"dataN\":\""
    part_4 = "\"}"

    # dataNi example: "20230425"
    dataNi = str(year) + str(month) + str(day)
    # dataN example: "2023-04-25"
    dataN = str(year) + '-' + str(month) + '-' + str(day)
    # no ',' before first json structure
    is_first = True
    code = 1
    # write json structures
    with open("data/dest.txt", "r", encoding="utf-8") as ifile, \
        open("data/result.json", "w", encoding="utf-8") as dfile:
        dfile.write("[")
        while True:
            line = ifile.readline()
            line = re.sub(r' \"', '«', line)
            line = re.sub(r'^\"', '«', line)
            line = re.sub(r'\" ', '»', line) 
            # »
            line = re.sub(r'\"$', '»', line) 

            if not line:
                break
            if is_first:
                dfile.write(part_1 + str(code) + part_1_1 + dataNi + part_2 + line.strip() + part_3 + dataN + part_4)
                code = code + 1
                is_first = False
            else:
                dfile.write("," + part_1 + str(code) + part_1_1 + dataNi + part_2 + line.strip() + part_3 + dataN + part_4)
                code = code + 1
        dfile.write("]")