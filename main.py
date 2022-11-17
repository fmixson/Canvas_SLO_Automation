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

class GradesHTML:

    def __init__(self, gradesLink):
        self.gradesLink = gradesLink

    def GradesSourcePage(self):
        driver.get(self.gradesLink)
        downArrow = driver.find_element(By.XPATH,'//*[@id="uk27gzZUsVm7"]/span/span/span[2]/span/span/svg').click()



        # pageLoading = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, "dialogue_for_help_0"))
        pageLoading = element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'screenreader-only')))
        # exportButton = driver.find_element(By.XPATH, '//*[@id="uCy2yKCKDDTu"]').click()
        # exportButton2 = driver.find_element(By.XPATH,'//*[@id="upTKLyjbbGUZ"]')
        # print('Export Button', exportButton2)


        # page_source = driver.page_source
        # exportButton = driver.find_element(By.XPATH, '/html/body/span/span/span/span[2]/ul/li[2]').click()
        # gradesSoup = BeautifulSoup(page_source,'lxml')
        # span = gradesSoup.find_all('button')

        # < span
        #
        # class ="sJGfW_blJt" id="umT6Hyuf2fZG" > < span data-menu-id="export-all" > Export Entire Gradebook < / span > < / span >
        # print('Gradebook Actions Button',buttons)
        print()



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
aTags = dashboard.find_all('a', {'class':'ic-DashboardCard__link'})
SLO_Courses = []
for atag in aTags:
    # print('A Tag', atag)
    term = atag.find('div',{'class':'ic-DashboardCard__header-term ellipsis'})
    # print('TERM', term)
# cards = dashboard.find_all('div', {'class', 'ic-DashboardCard'})
# print('CARDS',cards)

    termText = term.get_text(strip=True)
    # print('TEXT', termText)

    if '2016 Fall' in termText:
        # print('2016 Fall Term', term)

# print('SLO Courses', SLO_Courses)
# for course in SLO_Courses:
#     print('course', course)
    # courseLink = title3['href']
    # print(courseLink)
    # driver.get(courseLink)
    # courseLink.click()
        courseLink = atag['href']
        fullCourseLink = 'https://cerritos.instructure.com' + courseLink +'/grades'
        SLO_Courses.append(fullCourseLink)
        print('SLO Courses', SLO_Courses)

for link in SLO_Courses:
    grades = GradesHTML(gradesLink=link)
    grades.GradesSourcePage()

    # print('Full Course Link', fullCourseLink)
    # activeLink = driver.get(fullCourseLink)
    # gradeLink = fullCourseLink + '/grades'
    # activeGradeLiink = driver.get(gradeLink)
    # downloadGrades = driver.find_element(By.ID,'gradebook-toolbar')
    # print('Grade Sheet', downloadGrades)












# canvas_courses = []
# for dash in dashboard:
#     # print('DASH', dash)
#     # print()
#     # term = dash.find('div', {'class', 'ic-DashboardCard__header-term ellipsis', 'title='''})
#     title = dash.find('div', {'class', 'ic-DashboardCard__header_content'})
#     title2 = title.find('h3', {'class', 'ic-DashboardCard__header-title ellipsis'})
#     title3 = title2.get_text(strip=True)
#     # print('title', title)
    # print()
    # print('title2', title2)
    # print()
    # print('TITLE', title3)
    # if 'Equity' in title3:
    #     print('Equity', title3)
        # courseLink = title3['href']
        # print(courseLink)
        # driver.get(courseLink)
        # courseLink.click()
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
    #     print('Course Link', courseLink)
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