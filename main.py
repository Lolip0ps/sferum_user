from bs4 import BeautifulSoup

with open('SF.htm', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

# user_name = soup.find('div', class_='Entity__title').text.strip()
# print(user_name)

all_user_name = soup.find_all(class_="Entity__title")


file = open('users.txt', 'w', encoding='utf-8')
for user in all_user_name:
    file.write(user.text.strip() + '\n')