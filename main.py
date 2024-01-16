from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

now = datetime.now()
now_plus_10 = now + timedelta(minutes = 5)
print(now_plus_10)
print(now)
driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, "div[onmouseup]")
store = driver.find_elements(By.ID, "store")
text = store[0].text.splitlines()
costs = {}
for n in range(0, 8):
    item1 = text[n].split("-")[0].strip()
    cost = text[n].split("-")[1].strip()
    costs[item1] = (cost)
    text.remove(text[n + 1])
    for n in cost:
        if n == ",":
            item3 = cost.replace(",", "")
            costs[item1] = (int(item3))
points = driver.find_element(By.ID, "money")
points1 = points.text
n = 0
max = 0
flag = True
while flag:
    points1 = points.text
    cookie.click()
    if n == 170:
        n = 0
        for key, value in costs.items():
            if int(points1.split(',')[0].strip()) >= int(costs[key]):
                if max<=int(costs[key]):
                   max=int(costs[key])
                   print(max)
                   item = driver.find_element(By.CSS_SELECTOR, f"#buy{key}[onclick]")
                   item.click()
                   cookie.click()
    n += 1
