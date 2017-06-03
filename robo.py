"""
Por Ramon
"""
# pylint: disable=C0103

from robobrowser import RoboBrowser #classe principal para manipular as páginas
from robobrowser.forms.fields import Input #classe responsável por adicionar campos nas páginas

##instancia a classe e abre a página
browser = RoboBrowser()
browser.open('https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/producaoIntelectual/listaProducaoIntelectual.jsf')



####DEFINE CONTEÚDO DOS CAMPOS
ANO = '2017'
INSTITUICAO = '28001010 UNIVERSIDADE FEDERAL DA BAHIA (UFBA)'
PROGRAMA = '205551'


# obtém o form pelo id
form = browser.get_form(id="form")

##COMO O CAMPO DO PROGRAMA É GERADO COM JAVASCRIPT / AJAX,
# IREMOS INSERIR O CAMPO MANUALMENTE NA PÁGINA HTML
novo_input = Input('<input name="form:j_idt23:j_idt95">')
form.add_field(novo_input)
##

##INSERE OS VALORES DOS CAMPOS
form['form:j_idt23:ano'].value= ANO
form['form:j_idt23:inst:input'].value = INSTITUICAO
form['form:j_idt23:j_idt95'].value = PROGRAMA

##ENVIA O FORM
browser.submit_form(form,form['form:consultar'])

##PRINTA O CONTEÚDO DEPOIS DO SUBMIT
print(browser.parsed)
