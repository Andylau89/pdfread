# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os


# files = getfiles(path)
# print(type(files))
# print(files)
import re

import pdfminer
import pdfplumber



# import pdfplumber
# with pdfplumber.open(r"C:\Users\heliu001\Desktop\python\report\tt.pdf") as pdf:
#     for page in pdf.pages:
#         text = page.extract_text()#提取文本
#         print(text)


import pdfplumber


def getfiles(path):
    filenames = os.listdir(path)
    return filenames

path = r"C:\Users\heliu001\Desktop\python\report"
files_list = getfiles(path)
files_quantity = len(files_list)
print(files_quantity)
print(files_list)

# for i in range(files_quantity):
#     file_handling = files_list[i]
#     path_handling = 'C:\\Users\\heliu001\\Desktop\\python\\report\\'+ file_handling
#     print(path_handling)
#
#     with pdfplumber.open(path_handling) as pdf:
#         for page in pdf.pages:
#             text = page.extract_text()#提取文本
#             txt_file = open("C:\\Users\\heliu001\\Desktop\\python\\report\\"+ file_handling+'.txt',mode='a',encoding='utf-8')
#             txt_file.write(text)

    # with pdfplumber.open(r"C:\Users\heliu001\Desktop\python\report\"+ file_handling) as pdf:
    #     for page in pdf.pages:
    #         text = page.extract_text()#提取文本
    #         txt_file = open(r"C:\Users\heliu001\Desktop\python\report\1.txt",mode='a',encoding='utf-8')
    #         txt_file.write(text)
#中华人民共和国1111111111111111111111111

for i in range(files_quantity):
    file_handling = files_list[i]
    path_handling = 'C:\\Users\\heliu001\\Desktop\\python\\report\\'+ file_handling
    print('************')

    print(file_handling)

    # with pdfplumber.open("C:\\Users\\heliu001\\Desktop\\python\\report\\Measurement report (As received)_1-13856418768-10.pdf") as pdf:
    with pdfplumber.open(path_handling) as pdf:
        page01 = pdf.pages[0]
        page01_text = page01.extract_text()#提取文本

        # print(type(page01_text))
        # print(page01_text)

        so=re.findall(r'Certificate Number(.*?)\n',page01_text,re.S)
        model=re.findall(r'Model Number(.*?)\n',page01_text,re.S)
        serial=re.findall(r'Serial Number(.*?)\n',page01_text,re.S)
        procedure=re.findall(r'Test Executive(.*?)\n',page01_text,re.S)


    print(model,serial,so,procedure)


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
