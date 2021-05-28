<p align="center">
<img align="center" src="https://raw.githubusercontent.com/guilhermedonizetti/Sendex/master/images/logoSendex.png">
  <br>
Programa para envio de e-mail desenvolvido como projeto de Laboratório de Engenharia de Software e Testes de Software, na Fatec Cruzeiro.
  <br>
  Status do Projeto: Finalizado :heavy_check_mark:
 </p>
 <br>
 <b>Objetivo:</b> O programa visa o envio de e-mails com arquivos em anexo, dispensando a necessidade de inicar um navegador para realização da atividade.
 <br><br>
  <b>Justificativa:</b> Entendemos que o grande número de programas sendo executados em um computador amplia a superfície de ataque, expondo o dispositivo a riscos maiores. Assim, pensando em um ambiente crítico de segurança lógica, é interessante a execução apenas de serviços estritamente essenciais. Como o envio de e-mails é uma atividade recorrente, foi pensado no que poderia ser feito para reduzir a superfície de ataque durante essa atividade. O próprio navegador apresenta links e arquivos maliciosos que em algum momento atinge a fragilidade humana (do usuário), possui autocomplete de emails e senhas, e outros; dessa forma, entregar uma mensagem sem passar por essa exposição é interessante do ponto de vista da Segurança.
  <br><br>
 <b>Benefícios:</b><br>
 :heavy_check_mark: Realiza login somente quando for tentar o envio de e-mail<br>
 :heavy_check_mark: O programa nunca esquece de fazer logout<br>
 :heavy_check_mark: Depende menos de internet, pois a interface não está vinculada ao browser<br>
 :heavy_check_mark: O tempo para iniciar o programa, escrever e enviar é menor<br>
 
 <br>
 
 <b>Usar: </b> Após clonar o projeto deverá executar o arquivo <code>interface.py</code> e entrar digitando a senha <b>sendex</b>. Após entrar, clique no botão Autenticação para permitir que o programa se conecte com o seu servidor SMTP, isso deverá ser feito apenas uma vez no primeiro acesso. Siga as instruções:<br>
 :point_right: Conta do atual G-mail: digite sendex<br>
 :point_right: Senha do atual e-mail: digite sendex<br>
 :point_right: Registro atual: digite sendex<br>
 :point_right: Conta do novo G-mail: informe o gmail registrado no seu servidor SMTP<br>
 :point_right: Senha do novo e-mail: informe a senha registrado no seu servidor SMTP<br>
 :point_right: Novo registro: informe uma senha para entrar no programa (não pode esquecer)<br>
 Certifique-se de ter um servidor SMTP instalado e configurado em sua máquina, no projeto o teste foi feito com sSMTP.
 
 <br>
 <b>Servidor SMTP: </b>Caso você ainda não tenha sua conexão com um servidor SMTP, <a href="https://guilhermedonizettiads.medium.com/protocolo-e-agente-smtp-9fb424693109">veja aqui como instalar e configurar um agente.</a>
 
 <br><br>
 
 <p align="center">
 <b>Análise e Desenvolvimento de Sistemas - Fatec Cruzeiro</b>
  <br>
  Python, SMTP, Linux.
  </p>
