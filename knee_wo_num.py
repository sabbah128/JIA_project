from PIL import Image
import os


folder_img = '.\\knee'
imgs = os.listdir(folder_img)

Knee_wo = 'Knee_wo'

if not os.path.isdir(Knee_wo):
    os.mkdir(Knee_wo)

num = 0
for img in imgs:
    s = img.split('.')
    im = Image.open(folder_img + '\\' + img)
    if img.split('.')[-2] == '1':        
        im.save(Knee_wo + '\\' + s[0]+'.'+'ant'+'.jpg', mode='L')
        num += 1
    elif img.split('.')[-2] == '2':
        im = im.transpose(0)
        im.save(Knee_wo + '\\' + s[0]+'.'+'post'+'.jpg', mode='L')
        num += 1
    else:
        print('unknown')

print(num)
        


