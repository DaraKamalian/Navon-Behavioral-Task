from csv import DictWriter, writer
import csv, os, glob
from xlsxwriter.workbook import Workbook

time = 0
filename = ''
practiceDuration = 0
respversion = 0
taskversion = 0
trialcounter = 0
blockcounter = 0
trialfinished = 0

def append_dict_as_row(file_name, dict_of_elem, headers):
    with open(file_name, 'a+', newline='') as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=headers)
        dict_writer.writerow(dict_of_elem)


def createFile(filename):
    with open(filename, 'w', newline='') as file:
        Headers = ['ImageFile', 'Congruency', 'Visual Field', 'Block', 'G.L.Block', 'Trial', 'Key-Resp', 'Cor-Ans', 'Accuracy',
                   'R-time', 'Trial-Start', 'Key-Resp-Start']

        writer = csv.DictWriter(file, fieldnames=Headers)
        writer.writeheader()


def convertToExcel():
    for csvfile in glob.glob(os.path.join('.', '*.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()


def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def validateFields(list):
    emptylist = []
    for item in list:
        if item == '':
            emptylist.append(item)

    if emptylist:
        return False
    else:
        return True