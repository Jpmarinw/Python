from selenium import webdriver
import time

#abrir o navegador
navegador = webdriver.Chrome()
navegador.get('https://www.hashtagtreinamentos.com/?origemurl=75502579145&gad_source=1&gad_campaignid=2057505825&gbraid=0aaaaadllh88kank-vtp_iedi6daz7k4cf&gclid=cj0kcqjw5ubabhdiarisahmighykbym-trlfzufyg1a5w6ddnaa_lxvskcijxf8c_lpls__t12uz9esaati-ealw_wcb')

#colocar o navegador em tela cheia
navegador.maximize_window()

#selecionar um elemento na tela
botao_verde = navegador.find_element("class name", "botao-verde")
botao_verde.click()

#encontrar varios elementos
listar_botoes = navegador.find_elements("class name", "header__titulo")

for botao in listar_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break

#selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

# navegadar pra um site diferente
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

#escrever em um campo/formulario
navegador.find_element("id", "firstname").send_keys("João Pedro")
navegador.find_element("id", "email").send_keys("jpmariw@gmail.com")
navegador.find_element("id", "phone").send_keys("9299999999")


bota_quero_clicar = navegador.find_element("id", "_form_2475_submit")

#colocar um elemento na tela
navegador.execute_script("arguments[0].scrollIntoView({ block: 'center'})", bota_quero_clicar)

#aguardar 10 segundos
time.sleep(30)