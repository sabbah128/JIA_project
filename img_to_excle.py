import os
import pandas as pd
from PIL import Image


# def change_name():
#     os.mkdir('knee_name_ok')
#     imgs = os.listdir('.\\knee_new')
#     for i in imgs:
#         sttr = i.split('.')        
#         s = i.split('.')[0]
#         s = s.replace('^', '_')
#         s = s.upper()
#         s = s+'.'+'.'.join(sttr[2:])
#         im1 = Image.open('knee_new'+'\\'+ i)
#         im1.save('.\\knee_name_ok'+'\\'+ s, mode='L')


def set_label():
    names = []

    for images in os.listdir('knee_name_ok'):
        names.append(images.split('.')[0].lower())

    names = list(set(names))
    names.sort()
    print('knee_name_ok : ', len(names))

    df = pd.DataFrame(names, columns=['names'])
    writer = pd.ExcelWriter('knee_name_ok.xlsx')
    df.to_excel(writer, sheet_name='knee_name_ok', index=False)
    writer.save()

set_label()
print('Make excle file is done.')
