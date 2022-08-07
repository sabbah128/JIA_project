from PIL import Image
import os


folder_img = '.\\knee'
imgs = os.listdir(folder_img)

Knee_Ant_Post = 'Knee_Ant_Post'
if not os.path.isdir(Knee_Ant_Post):
    os.mkdir(Knee_Ant_Post)

ant = post = 0
for img in imgs:
    s = img.split('.')
    im = Image.open(folder_img + '\\' + img)
    if img.split('.')[-2] == '1':        
        im.save(Knee_Ant_Post + '\\' + s[0]+'.'+s[1]+'.'+'ant'+'.jpg', mode='L')
        ant += 1
    elif img.split('.')[-2] == '2':
        im = im.transpose(0)
        im.save(Knee_Ant_Post + '\\' + s[0]+'.'+s[1]+'.'+'post'+'.jpg', mode='L')
        post += 1
    else:
        print('unknown')

print(ant, post)
        


