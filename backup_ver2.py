# Использование стандартного модуля zipfile
import os
import time
import zipfile

# Собираем файлы и каталоги для копирования в список
source = ['"C:\\Users\\Alexey\\Documents\\For_Backup"']

# Путь для папки с резервом
target_dir = r'C:\\Users\\Alexey\\Documents\\Backup'

# Создаем имя для файла
today = target_dir + os.sep + time.strftime('%Y%m%d') + '.zip'

# Текущее время. используеться для имени архива
now = time.strftime('%H%M')

# Имя для архива
# с запросом комментария
comment = input('enter your comment there: ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'    

# Создаем каталог с днем, если его еще нет
if not os.path.exists(today):
    os.mkdir(today)
    print('каталог успешно создан', today)





