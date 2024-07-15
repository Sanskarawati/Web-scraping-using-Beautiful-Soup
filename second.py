from bs4 import BeautifulSoup
import requests
import time
unfamilar_skill=input('Put the required Skill>')
print(f'Filtering out {unfamilar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_ ="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        job_date=job.find('span',class_='sim-posted').span.text
        if 'few' in job_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href']
            if unfamilar_skill not in skills:
                with open(f'posts/{index}.txt','w')as f:
                    f.write(f'Company_name: {company_name.strip()}\n')
                    f.write(f'Skills: {skills.strip()}')
                    f.write(f'Published_date: {job_date.strip()}\n')
                    f.write(f'More_info: {more_info}')
                    f.write(' ')
                print(f'File saved {index}')
if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait=10
        print('waiting')
        time.sleep(time_wait*60)