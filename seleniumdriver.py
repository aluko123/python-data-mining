from selenium import webdriver #allows launching browser
from selenium.webdriver.common.by import By #allow search with params
from selenium.webdriver.support.ui import WebDriverWait #allow page load
from selenium.webdriver.support import expected_conditions as EC #determine that page has loaded
from selenium.common.exceptions import TimeoutException #handling timeout situation


#easily open a chrome window headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
#chromedriver_path = r'C:\Users\adeda\Dropbox\PC\Downloads\chromedriver_win32' #add your path here and specify using service, or you can just default it in your env 

def create_webdriver():
    return webdriver.Chrome(options = chrome_options)

#Open the website
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")


#Extract all projects on GitHub machine learning collections
projects = browser.find_elements("xpath", "//h1[@class='h3 lh-condensed']")

#print(projects)

#Extract info for each project
project_list = {}
for proj in projects:
    proj_name = proj.text #Project name
    proj_url = proj.find_element(By.XPATH, "./a").get_attribute('href')  # Project URL
    project_list[proj_name] = proj_url


#Close connection
browser.quit()


from IPython.display import display
import pandas as pd


#We can now extract the data from project_list
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

#Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop = True)


#display
#display(project_df)

#Export to CSV
project_df.to_csv('project_list.csv')



