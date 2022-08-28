import os
import pandas as pd
from PIL import Image


def change_name():
    os.mkdir('ankle_name_ok')
    imgs = os.listdir('.\\ankle')
    for i in imgs:
        sttr = i.split('.')        
        s = i.split('.')[0]
        s = s.replace('^', '_')
        s = s.upper()
        s = s+'.'+'.'.join(sttr[2:])
        im1 = Image.open('ankle\\'+ i)
        im1.save('.\\ankle_name_ok'+'\\'+ s, mode='L')


def set_label():
    names = []

    for images in os.listdir('ankle_name_ok'):
        names.append(images.split('.')[0].lower())

    names = list(set(names))
    names.sort()
    print('ankle_name_ok : ', len(names))

    df = pd.DataFrame(names, columns=['names'])
    writer = pd.ExcelWriter('ankle_name_ok.xlsx')
    df.to_excel(writer, sheet_name='ankle_name_ok', index=False)
    writer.save()

change_name()
set_label()
print('Make excle file is done.')
