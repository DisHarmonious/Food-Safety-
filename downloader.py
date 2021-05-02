from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/shokuhin/yunyu_kanshi/index_00017.html")
elems = driver.find_element_by_class_name("m-grid__col1").find_elements_by_xpath("//a[@href]")
for elem in elems:
    if elem.get_attribute("href").endswith("xls"): elem.click()







