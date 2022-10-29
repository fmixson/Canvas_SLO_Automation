from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
import requests

class CanvasCourse:

    def __init__(self, courseLink, courseName):
        self.courseLink = courseLink
        self.courseName = courseName

    def OpenCanvasCourse(self):
        print(self.courseName)




s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://cerritos.instructure.com/')
# pageLoading = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, "dialogue_for_help_0"))
element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'screenreader-only')))
page_source = driver.page_source
# page = requests.get('C:/Users/family/Desktop/Dashboard.html')
soup = BeautifulSoup(page_source, 'lxml')
tag = soup.body.h2
dashboard = soup.find('div', {'class', 'ic-DashboardCard__box__container'})
element2 = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'screenreader-only')))
term = dashboard.find_all('div', {'class', 'ic-DashboardCard__header-term ellipsis'})
canvas_courses = []
for dash in dashboard:
    # print('DASH', dash)
    print()
    # term = dash.find('div', {'class', 'ic-DashboardCard__header-term ellipsis', 'title='''})
    title = dash.find('div', {'class', 'ic-DashboardCard__header_content'})
    title2 = title.find('h3', {'class', 'ic-DashboardCard__header-title ellipsis'})
    title3 = title2.get_text(strip=True)
    print('TITLE', title3)
    if 'Equity' in title3:
        courseLink = title3['href']
        print(courseLink)
        driver.get(courseLink)
        courseLink.click()
    # courseLink = dash.find('a', {'class', 'ic-DashboardCard__link external'})
    #
    # # courseLink2 = driver.find_element(By.LINK_TEXT('href'))
    # # courseLink.click()
    # # print('Course Link2', courseLink2)
    # print()
    # print('TERM', term)
    # print()
    # print('Course Link', courseLink)
    # print()
    # print(term)
    # if 'Equity' in title3:
    #     # print('in term')
    #     courseLink = dash.find('a', {'class', 'ic-DashboardCard__link'})
    #     canvas_courses.append(courseLink)
    #     print('CANVAS COURSES', canvas_courses)
    #     print()
    #     # linkGroup = []
    #     # textList = []
    #     for item in canvas_courses:
    #         print(item)
    #     #     # link = item.has_attr('href')
    #     #     # print(link)
    #         courseLink = item['href']
    #         print(courseLink)
    #         # driver.get(courseLink)
    #         pageLoading = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CLASS_NAME, "event-list-view-calendar icon-calendar-day standalone-icon"))
    #         clickGrades = driver.find_element(By.XPATH, '//*[ @ id = "section-tabs"] / li[5] / a').click()
    #         pageLoading2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CLASS_NAME, "pronto-chat-iframe mini-window in-sidebar"))

        #     stripped = courseLink.strip()
        #     print(courseLink)

            # print('stripped', stripped)
            # print('type', type(stripped))
            # item['href'].click()
            # print()
            # link = item.has_attr('href')
            # linkGroup.append(item['href'])
        #     courseLink = dash.find('a', {'class', 'ic-DashboardCard__link external'})
        #     print('course link', courseLink)
        #     course = item.find('h3', {'class', 'ic-DashboardCard__header-title ellipsis'})
        #     course = course.get_text(strip=True)
        #     print('course', course)
        #     # print('link', link)
        #     a = CanvasCourse(courseLink, course)
        #     a.OpenCanvasCourse()
        # print(linkGroup)
        # for link in linkGroup:
        #     print(link)







    # print()
    # print(term)
    # print(dashboard)
    # print(type(term))
    # print(len(term))
    # canvas_courses = []
    # for t in term:
    #     print(t)
    #     term = t.get_text(strip=True)
    #     print(term)
    #     if term == '2022 Fall':
    #         canvas_courses.append(t)
    # print(canvas_courses)