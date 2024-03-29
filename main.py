from bs4 import BeautifulSoup
from datetime import date

with open('VK Мессенджер.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_user_name = soup.find_all(class_="Entity__title")

file = open(f'Учасники ВКС {date.today()}.txt', 'w', encoding='utf-8')
for user in all_user_name:
    file.write(user.text.strip() + '\n')
