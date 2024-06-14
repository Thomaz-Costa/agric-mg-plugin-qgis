# agric-mg-plugin-qgis

## Instalação
Para importar este plugin para o QGIS, clone este repositório no diretório de plugins do QGIS. O caminho padrão é:

Em máquinas GNU/Linux: 
`/home/USER/.local/share/QGIS/QGIS3/profiles/default/python/plugins`

Em máquinas Windows: `C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`

Teste o plugin ativando-o no QGIS plugin manager.

Customize-o editando o arquivo [select_agric.py](select_agric.py)

Para modificar a Interface de usuário, abra o arquivo [select_agric_dialog_base.ui](select_agric_dialog_base.ui) no Qt Designer. Utilize o Makefile para compilar o UI e arquivos de recursos quando realizar alterações

## Contribuição
Para contribuir, crie uma branch a partir da branch atual de desenvolvimento, de acordo com o gitflow

![alt text](./resources/gitflow.webp "GitFlow")