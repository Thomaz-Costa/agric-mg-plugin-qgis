# agric-mg-plugin-qgis

## Base de dados
Crie o diretório "PyQGIS" no drive C: e em C:\PyQGIS crie o diretório "Dados"

Em C:\Dados crie o diretório "Cartas_250000

Baixe e descompacte Dados.zip e Cartas_250000.zip nos diretórios pertinentes.
A url para baixas os arquivos .zip são:
https://drive.google.com/drive/folders/1rhVtptbE9rIAho6Sx3axs6Am4VHCHBiu?usp=drive_link
https://drive.google.com/drive/folders/1GxndxfQHOEYVWeU-oERezL_Fd_f9odVx?usp=drive_link

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

## REFERENCIAS
https://www.earthdata.nasa.gov/esds/competitive-programs/measures/nasadem
https://atlasdaspastagens.ufg.br/map
Projeto MapBiomas – Coleção [versão] da Série Anual de Mapas de Cobertura e Uso da Terra do Brasil, acessado em [data] através do link: [https://plataforma.brasil.mapbiomas.org]”
https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html
Hirano, C.; Amaral, F. C. S.; Palmieri, F.; Larach, J. O. I.;  Souza Neto, N. C. Delineamento macro-agroecológico do Brasil. Embrapa - Serviço Nacional de Levantamento e Conservação de Solos, Rio de Janeiro, 1991. 114p. (Embrapa-SNLCS. Boletim de Pesquisa, 37).
QGIS Development Team, <YEAR>. QGIS Geographic Information System. Open Source Geospatial Foundation Project. http://qgis.osgeo.org
https://docs.qgis.org/3.28/pdf/pt_BR/QGIS-3.28-PyQGISDeveloperCookbook-pt_BR.pdf
https://www.car.gov.br/#/
