from PIL import Image
import os


folder_img = '.\\ankle'
imgs = os.listdir(folder_img)

ankle_wo = 'ankle_wo'

if not os.path.isdir(ankle_wo):
    os.mkdir(ankle_wo)

num = 0
for img in imgs:
    s = img.split('.')
    im = Image.open(folder_img + '\\' + img)
    if img.split('.')[-2] == '1':        
        im.save(ankle_wo + '\\' + s[0]+'.'+'ant'+'.jpg', mode='L')
        num += 1
    elif img.split('.')[-2] == '2':
        im = im.transpose(0)
        im.save(ankle_wo + '\\' + s[0]+'.'+'post'+'.jpg', mode='L')
        num += 1
    else:
        print('unknown')

print(num)
        


