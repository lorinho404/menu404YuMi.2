  ​#!/usr/bin/env python3

 ​try​:
     ​        ​import​ ​os​, ​requests

 ​except​ ​ModuleNotFoundError​:
 ​        ​print​(​"​\033​[33mInstalando software necessário..."​)
 ​        ​os​.​system​(​"pip install requests &> /dev/null"​)

 ​try​: ​# importando o menu
 ​        ​from​ ​menu​ ​import​ ​*

 ​except​ ​ModuleNotFoundError​:
 ​        ​print​(​"​\033​[33mO arquivo foi corrompido."​); ​exit​(​0​)

 ​finally​:
 ​        ​import​ ​requests


 ​def​ ​mostrar_link​(​link​):
 ​        ​return​ ​f'​\033​[3;32mPara mais conteúdos acesse: ​\n​\033​[0m​{​link​}​\n​'


 ​def​ ​ler_arquivos​(​arquivo​, ​conteudo​: ​str​=​None​):
 ​        ​url​ ​=​ ​"https://raw.githubusercontent.com/Fundacao404/content_for_newbies/main/{}"

 ​        ​try​:
 ​                ​resp​ ​=​ ​requests​.​get​(​url​.​format​(​arquivo​))

 ​                ​if​ ​resp​.​status_code​ ​==​ ​200​:
 ​                        ​conteudo​ ​=​ ​resp​.​text

 ​        ​except​ ​requests​.​exceptions​.​ConnectionError​:
 ​                ​conteudo​ ​=​ ​"​\033​[33mVerifique sua conexão com a Internet e tente novamente."

 ​        ​if​ ​conteudo​ ​is​ ​not​ ​None​:
 ​                ​return​ ​conteudo

 ​        ​else​:
 ​                ​return​ ​"​\033​[33mO arquivo foi corrompido.​\n​"


 ​# main
 ​command_handler​ ​=​ {
 ​        ​1​: ​ler_arquivos​(​"download_RedHawk"​),
 ​        ​2​: ​ler_arquivos​(​"download_sqlmap"​),
 ​        ​3​: ​ler_arquivos​(​"download_PseudoDDoS"​),
 ​        ​4​: ​ler_arquivos​(​"download_cmdInicial"​),
 ​        ​5​: ​mostrar_link​(​"https://drive.google.com/folderview?id=1F-TFt_Skn-G3Udu8xKW0eTJ6vXUrjKQd"​),
 ​        ​6​: ​mostrar_link​(​"https://chat.whatsapp.com/BYZCvlzKqRBCmSYSSMUrVv"​),
 ​        ​7​: ​ler_arquivos​(​"download_vpn"​),
 ​        ​8​: ​ler_arquivos​(​"download_explicacao"​),
 ​        ​9​: ​"Adeus..." 

 ​};


 ​op​çã​o​ ​=​ ​0
 ​while​ ​op​çã​o​ ​!=​ ​9​:
 ​        ​count​ ​=​ ​0
 ​        ​if​ ​count​ ​==​ ​0​:
 ​                ​os​.​system​(​"cls||clear"​); ​print​(​menu​)
 ​                ​count​ ​+=​ ​1

 ​        ​try​:
 ​                ​op​çã​o​ ​=​ ​int​( 
 ​                ​input​( ​"​\033​[37mDigite sua opção: ​\033​[0m"​ ) 

 ​                        ); ​os​.​system​( ​"cls||clear"

 ​                ); ​print​( ​command_handler​[​op​çã​o​] )

 ​                ​if​ ​op​çã​o​ ​!=​ ​9​:
 ​                        ​voltar​ ​=​ ​0
 ​                        ​while​ ​voltar​ ​!=​ ​""​:
 ​                                ​voltar​ ​=​ ​input​(​"​\033​[31mTecle enter para voltar ao menu."​)

 ​                ​else​:
 ​                        ​os​.​system​(​"rm -rf __pycache__"​)


 ​        ​except​ (​KeyError​, ​ValueError​):
 ​                ​pass

 ​        ​except​ (​KeyboardInterrupt​, ​EOFError​):
 ​                ​exit​(​0​)