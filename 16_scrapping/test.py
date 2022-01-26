# Checar la instancia de Display en LINUX
from selenium import webdriver
# from webdriver_manager.Chrome import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()

print(type(driver))
# driver.get("http://selenium.dev")
driver.get("http://127.0.0.1:5500/16_scrapping/index.html")
# driver.find_element_by_id("contenedor-1")
contenedor = driver.find_element(by='id', value="contenedor-1")
contenedor.screenshot("contenedor-1.png")
print(contenedor.text)
print(dir(contenedor))
driver.save_screenshot("captura.png")
driver.quit()