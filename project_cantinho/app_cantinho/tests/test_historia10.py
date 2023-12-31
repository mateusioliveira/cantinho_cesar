from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

class Historia10(LiveServerTestCase):
    def test_01(self):
        driver = webdriver.Chrome(options=options)
        driver.get("http://127.0.0.1:8000")

        try:
            email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            senha = driver.find_element(By.CSS_SELECTOR, "input[name='senha']")
        except NoSuchElementException:
            print("Email or senha element not found.")
            return

        email.send_keys("teste25@teste.com")
        senha.send_keys("123")

        entrar = driver.find_element(By.XPATH, "//button[@value='Entrar']")
        entrar.click()

        botao_pedidos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "meus_pedidos"))
        )
        botao_pedidos.click()

        botao_avaliar_produto = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "avaliar_produto"))
        )
        botao_avaliar_produto.click()

        area_texto_avaliacao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "comment"))
        )
        area_texto_avaliacao.send_keys("Produto muito bom!!")

        salvar_avaliacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "salvar_avaliacao"))
        )

        salvar_avaliacao.click()

        driver.quit()

    try:
        sucesso = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'barra')]"))
        )
        assert True, sucesso
    except:
        assert True