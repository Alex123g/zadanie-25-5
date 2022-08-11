driver = webdriver.Firefox()
driver.get("http://https://petfriends.skillfactory.ru/")
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "myDynamicElement"))#добавляем элементы страницы
