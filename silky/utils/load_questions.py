import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import docx


def load_questions(cat_code):
    doc = docx.Document(f'silky/data/{cat_code[0]}.docx')
    pars = doc.paragraphs
    pars = [x.text for x in pars if x.text != '']
    pars = [pars[i:i + 2] for i in range(0, len(pars), 2)]
    for double_p in pars:
        print(double_p)
        prepare_data(double_p, cat_code)


def prepare_data(paragraph, cat_code):
    question = ""
    options = []
    for p in paragraph:
        if not p.startswith('Answer'):
            question = p.split('(')[0].split('.', 1)[1].strip()
            if not question.endswith((".", "!", "?")):
                question += "."
            options_str = p.split('(')[1].split(')')[0]
            options = [option.strip() for option in list(options_str.split('/'))]
        else:
            answer = p.split(':')[1].lower().strip()
            correct_answer = [options.index(option) + 1 for option in options if option.lower() == answer][0]
            fill_silky_answers(question, options, correct_answer, cat_code)


def fill_silky_answers(question, options, correct_answer, cat_code):
    s = webdriver.Chrome()
    print(cat_code)
    s.get("http://localhost:8000/admin")
    s.find_element(By.NAME, "username").send_keys("may")
    s.find_element(By.NAME, "password").send_keys("may")
    s.find_element(By.CSS_SELECTOR, ".submit-row input").click()

    s.find_element(By.CSS_SELECTOR, ".model-testquestion a").click()
    s.find_element(By.CSS_SELECTOR, "li a").click()

    s.find_element(By.ID, "id_question").send_keys(question)
    for index, option in enumerate(options):
        s.find_element(By.ID, f"id_answer_{index + 1}").send_keys(option)

    s.find_element(By.ID, "id_correct_answer").send_keys(correct_answer)
    s.find_element(By.NAME, "_save").click()
    s.quit()
