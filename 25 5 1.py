from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://https://petfriends.skillfactory.ru/")# указываем путь
myDynamicElement = driver.find_element_by_id("myDynamicElement")# элементы (фото, имя питомца, его возраст)
