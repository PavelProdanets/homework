import subprocess
import os
import random
from datetime import datetime, timedelta

# Виводити ім’я поточного користувача
subprocess.run(['whoami'])

# Виводити шлях до поточної директорії
subprocess.run(['pwd'])

# Створювати папку dz1 в поточній директорії
dz1_path = os.path.join(os.getcwd(), 'dz1')
os.makedirs(dz1_path, exist_ok=True)


# Функція для генерації імен файлів для кожного дня поточного місяця
def generate_log_filenames():
    today = datetime.today()
    first_day_of_month = today.replace(day=1)
    next_month = first_day_of_month.replace(month=today.month % 12 + 1)
    if next_month.month == 1:
        next_month = next_month.replace(year=next_month.year + 1)

    delta = next_month - first_day_of_month
    for i in range(delta.days):
        date = first_day_of_month + timedelta(days=i)
        yield date.strftime('%d-%m-%Y.log')


# В папці dz1 створювати файли для кожного дня поточного місяця
for filename in generate_log_filenames():
    file_path = os.path.join(dz1_path, filename)
    open(file_path, 'w').close()

# Змінювати овнера папки dz1 та всіх файлів в ній на root
subprocess.run(['sudo', 'chown', '-R', 'root:root', dz1_path])

# Видаляти 5 випадкових файлів з папки dz1
all_files = os.listdir(dz1_path)
print(all_files)
random_files_to_delete = random.sample(all_files, 5)
print(random_files_to_delete)
for file in random_files_to_delete:
     file_path = os.path.join(dz1_path, file)
     os.remove(file_path)