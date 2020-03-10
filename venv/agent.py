from selenium import webdriver
import time

def get_driver():
    agent = webdriver.Chrome(executable_path="./chromedriver")

    return agent

def get_source_code(agent, link):
    agent.get(link)

#def table_pages(source):
 #   pages = source.xpath()

if __name__ == "__main__":
    driver = get_driver()
    urls = [
        "http://kaf65.mephi.ru/tutorial/datasource_first/",
        "http://kaf65.mephi.ru/tutorial/datasource_second/",
        "http://kaf65.mephi.ru/tutorial/datasource_third/"
    ]

    for url in urls:
        print(get_source_code(driver, url))

    driver.close()