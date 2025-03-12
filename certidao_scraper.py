#!/usr/bin/env python
# coding: utf-8

# In[1]:

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os



chrome_options = Options()
chrome_options.add_argument("--start-maximized")


service = Service(ChromeDriverManager().install())


wd = webdriver.Chrome(service=service, options=chrome_options)

print("Carregando... Aguarde! :)")
time.sleep(18)
os.system('cls')
print("Bem Vindo !")

nome = input("Qual o nome?: ")
cpf = input("Qual o cpf?: ")
rg = input("Qual o RG?: ")
ddn = input("Qual a data de nascimento?: ")
nome_mae = input("Qual o nome da mãe?: ")
nome_pai = input("Qual o nome do pai?: ")
email = 'PREENCHA COM O SEU EMAIL'
genero = int(input("QUAL O GENERO? [1] MASCULINO [2] FEMININO: "))





while True:

    escolha = (int(input(f"Escolha qual certidão gostaria de tirar\n\nO sistema suporta 11 certidões\n\n[1] Quitação Eleitoral (TSE)\n[2] Crime Eleitoral (TSE)\n[3] Certidão de Ações Cível (ESAJ)\n[4] Certidão de Ação Criminal (ESAJ)\n[5] Certidão de Ação de Crime Militar (ESAJ)\n[6] Antecedentes Criminais – Estadual (SEJUSP)\n[7] Certidão de Segundo Grau – Ação cível (ESAJ)\n[8] Certidão de Segundo Grau - Ação de Criminal (ESAJ)\n[9] Certidão da Justiça Federal de Primeiro Grau em Mato Grosso do Sul\n[10] Certidão do Tribunal Regional Federal da 3ª região\n[11] Certidão Negativa Crime Militar Federal (STM)\n\nSua escolha: ")))
    
    if escolha == 1:
        
        wd.get("https://www.tse.jus.br/eleitor/certidoes/certidao-de-quitacao-eleitoral")
        certidao_eleitoral = wd.find_element(By.XPATH,'//*[@id="content"]/app-root/div/app-certidoes/div[1]/app-menu-option[1]/button/div/span[2]')
        certidao_eleitoral.click()
        time.sleep(2)
        
        nomeA = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[1]/input')
        nomeA.send_keys(nome)
        cpfA = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[2]/input')
        cpfA.send_keys(cpf)
        ddnA = wd.find_element(By.XPATH,'//*[@id="dataNascimento"]')
        ddnA.send_keys(ddn)
        nome_maeA = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[4]/div/input')
        nome_maeA.send_keys(nome_mae)
        nome_paiA = wd.find_element(By.XPATH,'//*[@id="nomePai"]')
        nome_paiA.send_keys(nome_pai)
        time.sleep(5)
        concluir = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]')
        concluir.click()
        
        
       
        
    elif escolha == 2:
        
        wd.get("https://www.tse.jus.br/eleitor/certidoes/certidao-de-crimes-eleitorais")
        certidao_crime_eleitoral = wd.find_element(By.XPATH,'//*[@id="content"]/app-root/div/app-certidoes/div[1]/app-menu-option[2]/button/div/span[2]')
        certidao_crime_eleitoral.click()
        time.sleep(2)
        
        nomeB = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[1]/input')
        nomeB.send_keys(nome)
        cpfB = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[2]/input')
        cpfB.send_keys(cpf)
        ddnB = wd.find_element(By.XPATH,'//*[@id="dataNascimento"]')
        ddnB.send_keys(ddn)
        nome_maeB = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[4]/div/input')
        nome_maeB.send_keys(nome_mae)
        nome_paiB = wd.find_element(By.XPATH,'//*[@id="nomePai"]')
        nome_paiB.send_keys(nome_pai)
        time.sleep(5)
        concluirB = wd.find_element(By.XPATH,'//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]')
        concluirB.click()

    elif escolha == 3:

        wd.get("https://esaj.tjms.jus.br/sco/abrirCadastro.do")
        comarca_tab1 = wd.find_element(By.XPATH,'//*[@id="id_sco.pedido.label.cdComarca"]')
        comarca_tab1.click()
        comarca_cac = wd.find_element(By.XPATH,'//*[@id="id_sco.pedido.label.cdComarca"]/option[56]')
        comarca_cac.click()
        
        certidao_cac_tab2 = wd.find_element(By.XPATH,'//*[@id="cdModelo"]')
        certidao_cac_tab2.click()
        
        certidao_acao_civel = wd.find_element(By.XPATH,'//*[@id="cdModelo"]/option[2]')
        certidao_acao_civel.click()
        time.sleep(1)
        
        nome_cac = wd.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        nome_cac.click()
        nome_cac.send_keys(nome)
        cpf_cac = wd.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        cpf_cac.click()
        cpf_cac.send_keys(cpf)
        rg_cac = wd.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        rg_cac.send_keys(rg)
        
        if genero == 1:
            gen_cac = wd.find_element(By.XPATH,'//*[@id="flGeneroM"]')
            gen_cac.click()
        else:
            gen_cac = wd.find_element(By.XPATH,'//*[@id="flGeneroF"]')
            gen_cac.click()
        
        nome_mae_cac = wd.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
        nome_mae_cac.send_keys(nome_mae)
        nome_pai_cac = wd.find_element(By.XPATH,'//*[@id="nmPaiCadastro"]')
        nome_pai_cac.send_keys(nome_pai) 
        email_cac = wd.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        email_cac.send_keys(email)
        confirmando_info_cac = wd.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]')
        confirmando_info_cac.click()

    elif escolha == 4:
        
        wd.get("https://esaj.tjms.jus.br/sco/abrirCadastro.do")
        comarca_tab1 = wd.find_element(By.XPATH,'//*[@id="id_sco.pedido.label.cdComarca"]')
        comarca_tab1.click()
        comarca_cac = wd.find_element(By.XPATH,'//*[@id="id_sco.pedido.label.cdComarca"]/option[56]')
        comarca_cac.click()

        certidao_ac_tab = wd.find_element(By.XPATH,'//*[@id="cdModelo"]')
        certidao_ac_tab.click()

        certidao_acao_criminal = wd.find_element(By.XPATH,'//*[@id="cdModelo"]/option[3]')
        certidao_acao_criminal.click()
        time.sleep(1)

        nome_ac = wd.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        nome_ac.click()
        nome_ac.send_keys(nome)
        cpf_ac = wd.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        cpf_ac.click()
        cpf_ac.send_keys(cpf)
        rg_ac = wd.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        rg_ac.send_keys(rg)

        if genero == 1:
            gen_ac = wd.find_element(By.XPATH,'//*[@id="flGeneroM"]')
            gen_ac.click()
        else:
            gen_ac = wd.find_element(By.XPATH,'//*[@id="flGeneroF"]')
            gen_ac.click()
        
        nome_mae_ac = wd.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
        nome_mae_ac.send_keys(nome_mae)
        nome_pai_ac = wd.find_element(By.XPATH,'//*[@id="nmPaiCadastro"]')
        nome_pai_ac.send_keys(nome_pai) 
        email_ac = wd.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        email_ac.send_keys(email)
        ddn_ac = wd.find_element(By.XPATH,'//*[@id="dataNascimento"]')
        ddn_ac.send_keys(ddn)

        
        confirmando_info_ac = wd.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]')
        confirmando_info_ac.click()

    elif escolha == 5:

        wd.get("https://esaj.tjms.jus.br/sco/abrirCadastro.do")
        comarca_tab1 = wd.find_element(By.XPATH,'//*[@id="id_sco.pedido.label.cdComarca"]')
        comarca_tab1.click()
        comarca_acm = wd.find_element(By.XPATH,'//*[@id="id_sco.pedido.label.cdComarca"]/option[56]')
        comarca_acm.click()

        certidao_ac_tab = wd.find_element(By.XPATH,'//*[@id="cdModelo"]')
        certidao_ac_tab.click()

        certidao_acao_crime_militar = wd.find_element(By.XPATH,'//*[@id="cdModelo"]/option[4]')
        certidao_acao_crime_militar.click()
        time.sleep(1)

        nome_acm = wd.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        nome_acm.click()
        nome_acm.send_keys(nome)
        cpf_acm = wd.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        cpf_acm.click()
        cpf_acm.send_keys(cpf)
        rg_acm = wd.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        rg_acm.send_keys(rg)

        if genero == 1:
            gen_acm = wd.find_element(By.XPATH,'//*[@id="flGeneroM"]')
            gen_acm.click()
        else:
            gen_acm = wd.find_element(By.XPATH,'//*[@id="flGeneroF"]')
            gen_acm.click()
        
        nome_mae_acm = wd.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
        nome_mae_acm.send_keys(nome_mae)
        nome_pai_acm = wd.find_element(By.XPATH,'//*[@id="nmPaiCadastro"]')
        nome_pai_acm.send_keys(nome_pai) 
        email_acm = wd.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        email_acm.send_keys(email)
        ddn_acm = wd.find_element(By.XPATH,'//*[@id="dataNascimento"]')
        ddn_acm.send_keys(ddn)

        
        confirmando_info_ac = wd.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]')
        confirmando_info_ac.click()

    elif escolha == 6:
        wd.get("http://antecedentes.sejusp.ms.gov.br/pages/MasterPages/IUPrincipal.aspx#")
    
        solicitar = wd.find_element(By.XPATH, '//*[@id="nav"]/li[1]/a')
        solicitar.click()
    
        
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.ID, "myFrame")))
        wd.switch_to.frame("myFrame")  
    
        
        nome_ace = WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtNome"]'))
        )
        nome_ace.click()
        nome_ace.send_keys(nome)
    
        nome_mae_ace = wd.find_element(By.XPATH, '//*[@id="txtMae"]')
        nome_mae_ace.send_keys(nome_mae)
    
        nome_pai_ace = wd.find_element(By.XPATH, '//*[@id="txtPai"]')
        nome_pai_ace.send_keys(nome_pai)
    
        ddn_ace = wd.find_element(By.XPATH, '//*[@id="txtDataNascimento"]')
        ddn_ace.click()
        ddn_ace.clear()
        for letra in ddn:  
            ddn_ace.send_keys(letra)
            time.sleep(0.1)
    
        selecionar_gen = wd.find_element(By.XPATH, '//*[@id="cmbSexo"]')
    
        if genero == 1:
            gen_ace = wd.find_element(By.XPATH, '//*[@id="cmbSexo"]/option[2]')
            gen_ace.click()
        else:
            gen_ace = wd.find_element(By.XPATH, '//*[@id="cmbSexo"]/option[3]')
            gen_ace.click()
    
        rg_ace = wd.find_element(By.XPATH, '//*[@id="txtRG"]')
        rg_ace.send_keys(rg)

    elif escolha == 7:
        wd.get("https://esaj.tjms.jus.br/scosg/abrirCadastro.do")
        
        certidao_cac2_tab2 = wd.find_element(By.XPATH,'//*[@id="cdModelo"]')
        certidao_cac2_tab2.click()
        
        certidao_acao_civel_2 = wd.find_element(By.XPATH,'//*[@id="cdModelo"]/option[2]')
        certidao_acao_civel_2.click()
        time.sleep(1)
        
        nome_cac2 = wd.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        nome_cac2.click()
        nome_cac2.send_keys(nome)
        cpf_cac2 = wd.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        cpf_cac2.click()
        cpf_cac2.send_keys(cpf)
        rg_cac2 = wd.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        rg_cac2.send_keys(rg)
        
        if genero == 1:
            gen_cac2 = wd.find_element(By.XPATH,'//*[@id="flGeneroM"]')
            gen_cac2.click()
        else:
            gen_cac2 = wd.find_element(By.XPATH,'//*[@id="flGeneroF"]')
            gen_cac2.click()
        
        nome_mae_cac2 = wd.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
        nome_mae_cac2.send_keys(nome_mae)
        nome_pai_cac2 = wd.find_element(By.XPATH,'//*[@id="nmPaiCadastro"]')
        nome_pai_cac2.send_keys(nome_pai) 

        ddn_ac2 = wd.find_element(By.XPATH,'//*[@id="dataNascimento"]')
        ddn_ac2.send_keys(ddn)
        
        email_cac2 = wd.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        email_cac2.send_keys(email)
        confirmando_info_cac2 = wd.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]')
        confirmando_info_cac2.click()
        
    elif escolha == 8:
        wd.get("https://esaj.tjms.jus.br/scosg/abrirCadastro.do")

        certidao_cac2_tab2 = wd.find_element(By.XPATH,'//*[@id="cdModelo"]')
        certidao_cac2_tab2.click()
        
        certidao_acao_criminal_2 = wd.find_element(By.XPATH,'//*[@id="cdModelo"]/option[3]')
        certidao_acao_criminal_2.click()
        time.sleep(1)
        
        nome_ac2 = wd.find_element(By.XPATH,'//*[@id="nmCadastroF"]')
        nome_ac2.click()
        nome_ac2.send_keys(nome)
        cpf_ac2 = wd.find_element(By.XPATH,'//*[@id="identity.nuCpfFormatado"]')
        cpf_ac2.click()
        cpf_ac2.send_keys(cpf)
        rg_ac2 = wd.find_element(By.XPATH,'//*[@id="identity.nuRgFormatado"]')
        rg_ac2.send_keys(rg)
        
        if genero == 1:
            gen_ac2 = wd.find_element(By.XPATH,'//*[@id="flGeneroM"]')
            gen_ac2.click()
        else:
            gen_ac2 = wd.find_element(By.XPATH,'//*[@id="flGeneroF"]')
            gen_ac2.click()
        
        nome_mae_ac2 = wd.find_element(By.XPATH,'//*[@id="nmMaeCadastro"]')
        nome_mae_ac2.send_keys(nome_mae)
        nome_pai_ac2 = wd.find_element(By.XPATH,'//*[@id="nmPaiCadastro"]')
        nome_pai_ac2.send_keys(nome_pai) 

        ddn_ac2 = wd.find_element(By.XPATH,'//*[@id="dataNascimento"]')
        ddn_ac2.send_keys(ddn)
        
        email_ac2 = wd.find_element(By.XPATH,'//*[@id="identity.solicitante.deEmail"]')
        email_ac2.send_keys(email)
        confirmando_info_ac2 = wd.find_element(By.XPATH,'//*[@id="confirmacaoInformacoes"]')
        confirmando_info_ac2.click()

    elif escolha == 9:
        wd.get("https://web.trf3.jus.br/certidao-regional/CertidaoCivelEleitoralCriminal/SolicitarDadosCertidao")
        
        lista_trf = wd.find_element(By.XPATH,'//*[@id="Tipo"]')
        lista_trf.click()
        certidao_trf = wd.find_element(By.XPATH,'//*[@id="Tipo"]/option[3]')
        certidao_trf.click()

        tipo_doc = wd.find_element(By.XPATH,'//*[@id="TipoDeDocumento"]')
        tipo_doc.click()

        opcao_doc = wd.find_element(By.XPATH,'//*[@id="TipoDeDocumento"]/option[2]')
        opcao_doc.click()

        doc_trf = wd.find_element(By.XPATH,'//*[@id="Documento"]')
        doc_trf.send_keys(cpf)

        abrangencia_lista = wd.find_element(By.XPATH,'//*[@id="TipoDeAbrangencia"]')
        abrangencia_lista.click()

        abrangencia = wd.find_element(By.XPATH,'//*[@id="TipoDeAbrangencia"]/option[3]')
        abrangencia.click()

    elif escolha == 10:
        wd.get("https://web.trf3.jus.br/certidao-regional/CertidaoCivelEleitoralCriminal/SolicitarDadosCertidao")

        lista_trf = wd.find_element(By.XPATH,'//*[@id="Tipo"]')
        lista_trf.click()
        certidao_trf = wd.find_element(By.XPATH,'//*[@id="Tipo"]/option[3]')
        certidao_trf.click()

        tipo_doc = wd.find_element(By.XPATH,'//*[@id="TipoDeDocumento"]')
        tipo_doc.click()

        opcao_doc = wd.find_element(By.XPATH,'//*[@id="TipoDeDocumento"]/option[2]')
        opcao_doc.click()

        doc_trf = wd.find_element(By.XPATH,'//*[@id="Documento"]')
        doc_trf.send_keys(cpf)

        abrangencia_lista = wd.find_element(By.XPATH,'//*[@id="TipoDeAbrangencia"]')
        abrangencia_lista.click()

        abrangencia = wd.find_element(By.XPATH,'//*[@id="TipoDeAbrangencia"]/option[4]')
        abrangencia.click()

    elif escolha == 11:
        wd.get("https://www2.stm.jus.br/ceneg_internet/emitir/index.php")
        time.sleep(2)

        nome_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input')
        nome_stm.send_keys(nome)

        cpf1_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input[1]')
        cpf1_stm.send_keys(cpf[:3])
        
        cpf2_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input[2]')
        cpf2_stm.send_keys(cpf[3:6])
        
        cpf3_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input[3]')
        cpf3_stm.send_keys(cpf[6:9])
        
        cpf_dv_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input[4]')
        cpf_dv_stm.send_keys(cpf[9:])

        ddn1_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input[1]')
        ddn1_stm.send_keys(ddn[:2])

        ddn2_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input[2]')
        ddn2_stm.send_keys(ddn[2:4])

        ddn3_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input[3]')
        ddn3_stm.send_keys(ddn[4:])
        
        

        nome_mae_stm = wd.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input')
        nome_mae_stm.send_keys(nome_mae)
    else:
        print('digite uma opção válida')

