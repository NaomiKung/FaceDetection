from datetime import  datetime
import os

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%d:%m:%Y,%H:%M:%S')
            f.writelines(f'\n{name}, {dtString}')

path = './service/attendance/Daily'

x = datetime.now()
table = "attendance" + '_' + x.strftime('%d%m%Y')
files = os.listdir(path)

def create_csv(files, table):
    for i in files:
        if i == table + '.csv':
            pass
        else:
            try:
                open( f'{path}/{date}.csv', 'x')
                print(f'Create file {date}')
            except :
                print("Have file")

def mark(path):
    x = datetime.now()
    date = "attendance" + '_' + x.strftime('%d%m%Y')
    with open(f'{path}/{date}.csv') as f:
        lines = f.readlines()
        for line in lines:
            entry = line.split(',')
            print(entry[0])

