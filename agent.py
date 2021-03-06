from selenium import webdriver
import time
from lxml.html import fromstring
import json

def get_driver():
    agent = webdriver.Chrome(executable_path="./resources/chromedriver")
    return agent

def get_source_code(agent, link):
    agent.get(link)
    return fromstring(agent.page_source)


def table_pages(source):
    pages = source.xpath("//ul/li/a/@href")
    return list(set(pages))

def get_data(agent, link):
    table_data = []

    source_code = get_source_code(agent, link)
    pages = table_pages(source_code)

    headers = source_code.xpath("//thead/tr/th/a/text()")
    for page in pages:
        full_link = link + page
        agent.get(full_link)
        rows = get_source_code(agent, full_link).xpath("//tbody/tr")
        for row in rows:
            cells = row.xpath("td/text()")
            item = dict()
            if cells[2] == "Operating":
                for i, cell in enumerate(cells):
                    item[headers[i]] = cell
                table_data.append(item)

    return table_data

def get_merge_data(all_data):
    result = dict()

    for item in all_data:
        if result.get(item["Name"]):
            result[item["Name"]] = {**result[item["Name"]], **item}
        else:
            result[item["Name"]] = item
        
        return result

def save_json(all_data):
    with open("resources/npps.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4)


if __name__ == "__main__":
    driver = get_driver()
    urls = [
        "http://kaf65.mephi.ru/tutorial/datasource_first/",
        "http://kaf65.mephi.ru/tutorial/datasource_second/",
        "http://kaf65.mephi.ru/tutorial/datasource_third/"
    ]

    sandbox = []

    for url in urls:
        data = get_data(driver, url)
        sandbox += data

    driver.close()
    merge_data = get_merge_data(sandbox)
    save_json(merge_data)