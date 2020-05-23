from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = 'Olá, essa mensagem está sendo escrita automaticamente por um script que eu fiz. Oque vc achou?'
        self.grupos = ['Isabella', 'Mateus Filhor']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="Isabella" class="_1wjpf _3NFp9 _3FXB1"><span class="matched-text _3FXB1">Isa</span>bella</span>

        # <div tabindex="-1" class="_1Plpp">

        # <span data-icon="send" class="">

        # <button class="_35EW6">

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f'//span[@title="{grupo}"]')
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            btn_enviar = self.driver.find_element_by_class_name('_35EW6')
            time.sleep(3)
            btn_enviar.click()
            time.sleep(3)

bot = WhatsappBot()
bot.EnviarMensagens()