# Genômica Comparativa - Tutorial 1

# OASIS 🌴 (Ortholog Alignment & Similarity Screener)

O [OASIS (*Ortholog Alignment & Similarity Screener*)](https://github.com/RodrigoOrvate/OASIS) é um pipeline de linha de comando interativo e robusto, projetado para pesquisadores de bioinformática. Desenvolvido em linguagem *Bash*, este sistema foi criado para buscar, alinhar e filtrar rigorosamente sequências ortólogas do NCBI, fornecendo conjuntos de dados confiáveis para alinhamentos múltiplos e análises filogenéticas.

Buscas web tradicionais pelo BLAST costumam introduzir ruídos causados por sequências sintéticas e parálogos. Para resolver isso, o OASIS automatiza o *download* utilizando a curadoria evolutiva do NCBI e aplica uma filtragem dupla baseada em limiares de Identidade e Similaridade/Positivos.

Ele foi desenvolvido por [Rodrigo Orvate Arruda](https://github.com/RodrigoOrvate), em colaboração com a equipe do [EvoMol-Lab](https://evomol-lab.imd.ufrn.br).

## *Input*

O programa aceita a entrada de um único número de acesso (*accession*), múltiplos acessos separados por espaço ou até arquivos em lote (*batch file*) contendo um acesso por linha. O *input* suporta sequências RefSeq de proteína (`NP_`, `XP_`, `WP_`), RefSeq de nucleotídeo/transcrito (`NM_`, `XM_`), acessos UniProtKB e IDs numéricos de genes do NCBI.

Em sua execução o *pipeline* realiza a resolução automática de Gene IDs e busca ortólogos majoritariamente pelo NCBI Datasets CLI, utilizando o *efetch* apenas como contingência. O OASIS permite ainda aplicar um filtro taxonômico opcional (ex: `Mammalia`) para limitar a busca a um clado de interesse, o que também ajuda a mitigar truncamentos em famílias de genes muito grandes. Adicionalmente, o OASIS possui uma rotina heurística que sinaliza ou remove isoformas e entradas redundantes agrupadas por organismo antes da etapa do BLAST.

**Avisos em Tempo Real:** Um sistema de alerta dinâmico é acionado para avisar ao usuário sobre quaisquer divergências encontradas na contagem de sequências extraídas.

## Instalação e Execução Local

Para rodar localmente, certifique-se de que sua máquina possui:

* Um terminal Linux ou macOS (shell bash).
* Instalação do `python3`.
* Acesso ativo à internet para conexão com as ferramentas E-utilities, Datasets do NCBI e a API do UniProt.

> **Nota:** *Os binários do NCBI Datasets CLI e do BLAST+ são instalados automaticamente no seu diretório de usuário durante a primeira execução, não exigindo privilégios de administrador.*

Clone o repositório para a sua máquina utilizando o comando `git clone https://github.com/RodrigoOrvate/OASIS.git`.

1. Navegue até a pasta criada com o comando `cd OASIS`.
2. Torne o arquivo do programa executável rodando `chmod +x OASIS.sh`.

### Como rodar o pipeline

* **Modo Totalmente Interativo:** 
  Basta executar `./OASIS.sh` no seu terminal. O script abrirá um menu guiado.
* **Modo Rápido / Não interativo:** É possível pular o menu passando os parâmetros diretamente. A estrutura é: `./OASIS.sh <ID_DE_ACESSO> <IDENTIDADE_MINIMA> <SIMILARIDADE_MINIMA>`.
  * *Exemplo com acesso único:* `./OASIS.sh NP_001416352.1 90 95`.
  * *Exemplo com arquivo em lote:* `./OASIS.sh meus_acessos.txt 90 95`.

Durante a execução (mesmo via parâmetros), o programa perguntará uma vez se você deseja exportar os arquivos FASTA (proteína e/ou CDS), pedirá um escopo taxonômico opcional e definirá como as isoformas devem ser tratadas (manter, sinalizar ou remover).

## Arquivos de Saída

Para cada acesso pesquisado, uma pasta de resultados no formato `OASIS_results_<timestamp>/<accession>/` será criada, contendo:

* Um arquivo `.txt` listando todos os acessos que passaram pelos seus filtros de Identidade e Similaridade.
* O arquivo FASTA de proteínas ou CDS de interesse, caso tenha sido configurado previamente.
* Um relatório de extensão `.tsv` contendo as sequências que foram sinalizadas como isoformas ou redundâncias.

## Ambientes Alternativos de Uso

Se você não quiser instalar as ferramentas em sua máquina, o OASIS oferece as seguintes alternativas:

### Google Colab

* O repositório inclui o notebook `OASIS_Colab.ipynb`, pronto para uso direto no Google Colab.
* Ao executá-lo, a primeira célula exibirá formulários visuais equivalentes às opções do CLI (limites, filtros taxonômicos e tratamento de isoformas).
* Os arquivos resultantes (FASTA, lista filtrada e relatórios) são baixados diretamente no seu computador no final da execução.

> **Aviso:** A versão de Colab avalia apenas um acesso por vez e não suporta arquivos em lote.

### Docker / Singularity

* Uma imagem pode ser construída localmente via Docker com o comando `docker build -t oasis:latest .`.
* Para rodar passando parâmetros e salvando dados, utilize: `docker run -it --rm -v "$(pwd)/data:/data" oasis:latest NP_001416352.1 90 95`.
* O programa também oferece suporte integral para criação e execução de contêineres via Singularity/Apptainer.

## Avisos Importantes e Limitações

* A triagem heurística de isoformas do pipeline serve para agilizar processos, mas a curadoria manual continua sendo recomendada antes da submissão dos dados a análises filogenéticas.
* O CLI do Datasets do NCBI tem uma limitação imposta de retorno máximo de 499 sequências em determinadas requisições. Apesar desse fator ser parcialmente contornado por meio das quebras nos filtros taxonômicos do OASIS, a limitação não é eliminada por completo.