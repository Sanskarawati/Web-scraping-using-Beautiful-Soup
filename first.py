from bs4 import BeautifulSoup

with open('first_scrapped.html', 'r') as html_file:
    content=html_file.read()
    soup=BeautifulSoup(content,'lxml')
    courses_html_tags=soup.find_all('div',class_='card')
    for course in courses_html_tags:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')


