import os
from glob import glob
import math
import shutil
from shutil import copyfile
from pathlib import Path


cam_path=glob("../TAGGED DATA/*/*/")
day=[]
night=[]
Test=[]
Train=[]
Train=[]
for x in cam_path:
    day.append(glob(x+"*.xml"))
    night.append(glob(x + "*.xml"))
for x in day:
    for y in x[0:math.ceil(len(x)*0.588)]:
        temp=y.split('/')[len(y.split('/'))-1]
        jpg= Path(y[0:len(y)-3]+'jpg')
        xml= Path(y[0:len(y) - 3] + 'xml')
        if jpg.is_file() and xml.is_file():
            copyfile(y[0:len(y)-3]+'jpg',"../Data_28_3/Train/"+temp[0:len(temp)-3]+'jpg')
            print('--')
            copyfile(y[0:len(y) - 3] + 'xml', "../Data_28_3/Train/" + temp[0:len(temp) - 3] + 'xml')
        # os.rename(y[0:len(y)-3]+'jpg',"../Train/"+temp[0:len(temp)-3]+'jpg')
        # os.rename(y[0:len(y) - 3] + 'xml', "../Train/" + temp[0:len(temp) - 3] + 'xml')
            Train.append(y)
    for y in x[math.ceil(len(x)*0.588):math.ceil(len(x)*0.882)]:
        temp = y.split('/')[len(y.split('/')) - 1]
        jpg = Path(y[0:len(y) - 3] + 'jpg')
        xml = Path(y[0:len(y) - 3] + 'xml')
        if jpg.is_file() and xml.is_file():
            copyfile(y[0:len(y) - 3] + 'jpg', "../Data_28_3/Train/" + temp[0:len(temp) - 3] + 'jpg')
            print('--')
            copyfile(y[0:len(y) - 3] + 'xml', "../Data_28_3/Train/" + temp[0:len(temp) - 3] + 'xml')
            Train.append(y)
    for y in x[math.ceil(len(x)*0.882):len(x)]:
        temp = y.split('/')[len(y.split('/')) - 1]
        jpg = Path(y[0:len(y) - 3] + 'jpg')
        xml = Path(y[0:len(y) - 3] + 'xml')
        if jpg.is_file() and xml.is_file():
            copyfile(y[0:len(y) - 3] + 'jpg', "../Data_28_3/Test/" + temp[0:len(temp) - 3] + 'jpg')
            print('--')
            copyfile(y[0:len(y) - 3] + 'xml', "../Data_28_3/Test/" + temp[0:len(temp) - 3] + 'xml')
            Test.append(y)
for x in night:
    for y in x[0:math.ceil(len(x)*0.588)]:
        temp = y.split('/')[len(y.split('/')) - 1]
        jpg = Path(y[0:len(y) - 3] + 'jpg')
        xml = Path(y[0:len(y) - 3] + 'xml')
        if jpg.is_file() and xml.is_file():
            copyfile(y[0:len(y) - 3] + 'jpg', "../Data_28_3/Train/" + temp[0:len(temp) - 3] + 'jpg')
            print('--')
            copyfile(y[0:len(y) - 3] + 'xml', "../Data_28_3/Train/" + temp[0:len(temp) - 3] + 'xml')
            Train.append(y)
    for y in x[math.ceil(len(x)*0.588):math.ceil(len(x)*0.882)]:
        temp = y.split('/')[len(y.split('/')) - 1]
        jpg = Path(y[0:len(y) - 3] + 'jpg')
        xml = Path(y[0:len(y) - 3] + 'xml')
        if jpg.is_file() and xml.is_file():
            copyfile(y[0:len(y) - 3] + 'jpg', "../Data_28_3/Train/" + temp[0:len(temp) - 3] + 'jpg')
            print('--')
            copyfile(y[0:len(y) - 3] + 'xml', "../Data_28_3/Train/" + temp[0:len(temp) - 3] + 'xml')
            Train.append(y)
    for y in x[math.ceil(len(x)*0.882):len(x)]:
        temp = y.split('/')[len(y.split('/')) - 1]
        jpg = Path(y[0:len(y) - 3] + 'jpg')
        xml = Path(y[0:len(y) - 3] + 'xml')
        if jpg.is_file() and xml.is_file():
            copyfile(y[0:len(y) - 3] + 'jpg', "../Data_28_3/Test/" + temp[0:len(temp) - 3] + 'jpg')
            print('--')
            copyfile(y[0:len(y) - 3] + 'xml', "../Data_28_3/Test/" + temp[0:len(temp) - 3] + 'xml')
            Test.append(y)

print(Train)
print(len(Train))
print(Train)
print(len(Train))
print(Test)
print(len(Test))
print(len(Train)+len(Train)+len(Test))
