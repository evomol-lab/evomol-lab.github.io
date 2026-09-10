# Pipeline do Marauders GenoMap

O [**Marauders GenoMap**](https://github.com/evomol-lab/MaraudersGenoMap) é uma interface gráfica (Python/PyQt6) que automatiza um fluxo completo de bioinformática: baixar dados do SRA, montar o genoma/transcriptoma e procurar domínios proteicos com o HMMER, tudo organizado em pastas por número de acesso SRA. Seu principal objetivo é a busca de homólogos com baixa identidade ou de proteínas com potencial biotecnológico em genomas e transcriptomas de espécies não-modelo.

Na prática, ele é uma "casca" gráfica que chama, nos bastidores, scripts de shell já prontos (pasta `scripts/`). Cada etapa cria subpastas dentro da pasta do código SRA, por exemplo: `SRRXXXXXX/01_QC_Reports`, `SRRXXXXXX/05_Assembly_Results`, `SRRXXXXXX/02_HMMER_Results`.

> O programa foi feito para rodar localmente (na sua máquina), de preferência via Docker ou Singularity/Apptainer, para não precisar instalar manualmente todas as dependências.

## O que já vem pronto na imagem

A imagem Docker/Singularity já inclui todas as ferramentas necessárias, então você não precisa instalar nada manualmente:

- **Montagem:** MEGAHIT, SPAdes, Trinity
- **Quantificação/mapeamento:** Salmon, Bowtie2, Samtools
- **Download/QC:** SRA Toolkit, FastQC, Trimmomatic, BBMap, MultiQC
- **Predição/busca de domínios:** Prodigal, HMMER, SeqTK
- **Interface e análise:** PyQt6, Pandas, Matplotlib, Biopython

## Passo 1 — Instalar e abrir o programa (via Docker)

A forma mais simples de usar o Marauders GenoMap é baixando a imagem já pronta do Docker Hub.

- Baixe a imagem:

```shell
docker pull evomol/marauders-genomap
```

- Antes de abrir a interface gráfica, libere o acesso local ao servidor X11 (necessário para a janela do programa aparecer na tela):

```shell
xhost +local:docker
```

- Execute a imagem:

```shell
docker run --rm -it \
    --network host \
    --user $(id -u):$(id -g) \
    -e DISPLAY=$DISPLAY \
    -e XAUTHORITY=/tmp/.Xauthority \
    -e HOME=/tmp \
    -e QT_X11_NO_MITSHM=1 \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v "${XAUTHORITY:-$HOME/.Xauthority}":/tmp/.Xauthority:ro \
    -v "$(pwd)":/data \
    -w /data \
    evomol/marauders-genomap:latest bash -c "python3 /app/marauders.py"
```

> *Repare no `-v "$(pwd)":/data`: a pasta em que você está no terminal é "espelhada" dentro do container. É ali que os arquivos baixados e os resultados vão aparecer, e não dentro de uma camada temporária do container.*

- Quando terminar de usar, revogue a permissão do X11:

```shell
xhost -local:docker
```

> Se preferir, o projeto também tem um `Makefile` com atalhos (`make docker-build`, `make docker-run`) e é compatível com Singularity/Apptainer, puxando a mesma imagem do Docker Hub com `singularity pull` ou `apptainer pull`.

## Passo 2 — Entendendo as 5 abas do programa

A interface é organizada em 5 abas, em sequência. O código SRA que você informa na primeira aba é reaproveitado automaticamente pelas abas seguintes — você não precisa digitá-lo de novo.

### Aba 1 — Download

Baixa os dados brutos do SRA e prepara os arquivos FASTQ compactados.

- Você informa o código de acesso SRA e o tipo de amostra;
- Para transcriptômica/metatranscriptômica, escolhe entre *paired-end* ou *single-end*;
- O programa cria uma pasta com o nome do acesso e executa `prefetch`, depois `fasterq-dump` (ou `fastq-dump` como alternativa), e compacta tudo com `pigz`.

**Resultado esperado:**

- `SRA_ID/SRA_ID_1.fastq.gz` e `SRA_ID/SRA_ID_2.fastq.gz` (paired-end), ou
- `SRA_ID/SRA_ID.fastq.gz` (single-end).

### Aba 2 — Assembly (Montagem)

Executa controle de qualidade, trimagem, normalização e a montagem propriamente dita.

- Você escolhe o montador: **MEGAHIT** (recomendado para metagenomas e execução rápida), **SPAdes** (genômica de isolados) ou **Trinity** (transcriptômica/metatranscriptômica);
- Ajusta threads e memória RAM (o programa sugere um valor de GB por thread);
- Pode marcar para remover os arquivos brutos e/ou a pasta de trimagem ao final;
- Roda, em sequência: FastQC → Trimmomatic → BBNorm → MultiQC → montador escolhido.

**Pastas criadas:** `01_QC_Reports`, `02_Trimmed_Reads`, `03_Normalized_Reads`, `04_MultiQC_Report`, `05_Assembly_Results`.

**Principais saídas:**

- MEGAHIT: `05_Assembly_Results/MEGAHIT_*/final.contigs.fa`
- SPAdes: `05_Assembly_Results/SPADES_*/scaffolds.fasta` (ou `contigs.fasta`)
- Trinity: arquivos `*.Trinity.fasta`

### Aba 3 — Protein Search (Busca de proteínas)

Prediz as proteínas a partir dos contigs montados e procura domínios usando um perfil HMM.

- Você fornece um arquivo `.hmm`;
- O programa localiza automaticamente o arquivo de contigs gerado na etapa anterior;
- Escolhe o modo do Prodigal: `single` (genômica) ou `meta` (metagenômica/metatranscriptômica);
- Executa o Prodigal (predição de proteínas) e depois o `hmmsearch` (busca de domínios).

**Pastas criadas:** `01_Predicted_Proteins`, `02_HMMER_Results`.

**Principais saídas:**

- `01_Predicted_Proteins/predicted_proteins.faa`
- `02_HMMER_Results/*_domain_hits.tbl`

### Aba 4 — Get Results (Obter resultados)

Extrai as sequências das proteínas que tiveram hits detectados pelo HMMER.

- Localiza automaticamente a tabela `.tbl` em `02_HMMER_Results` e o arquivo `predicted_proteins.faa`;
- Extrai os IDs únicos da primeira coluna da tabela do HMMER;
- Usa `seqtk subseq` para recuperar as sequências correspondentes.

**Saídas:** arquivo temporário `protein_ids_to_extract.txt` e o arquivo final `lectin_hits.faa` com as sequências extraídas.

### Aba 5 — Analysis & Cutting (Análise e recorte)

Permite visualizar os hits, selecionar alvos de interesse e extrair/recortar sequências específicas — tudo isso feito internamente pelo `marauders.py`, sem chamar um script externo.

- Carrega automaticamente a tabela `.tbl` da pasta `SRA_ID/02_HMMER_Results` (ou permite selecionar manualmente outra tabela);
- Filtra os hits com `full_E-value < 0.0001` e mostra os 25 melhores;
- Ao clicar em uma linha, o `target_name` é transferido para o campo de busca (o "Severus Snap(e) extractor");
- Localiza automaticamente `01_Predicted_Proteins/predicted_proteins.faa` (ou aceita um FASTA manual);
- Salva as sequências encontradas pelo termo buscado e, quando possível, recorta a região usando as coordenadas presentes na descrição do FASTA;
- Gera um histograma do comprimento das sequências, usando Matplotlib.

## Passo 3 — Estrutura final de pastas

Ao final de um fluxo completo para um acesso SRA, a estrutura de pastas fica assim:

```
SRA_ID/
├── 01_QC_Reports/
├── 02_Trimmed_Reads/
├── 03_Normalized_Reads/
├── 04_MultiQC_Report/
├── 05_Assembly_Results/
├── 01_Predicted_Proteins/
├── 02_HMMER_Results/
└── lectin_hits.faa
```

> Algumas pastas podem não aparecer, dependendo das opções escolhidas, do tipo de amostra e de quais abas você efetivamente executou.

## Observações úteis

- O programa depende de um display X11 quando executado via Docker — por isso os passos de `xhost` e das variáveis `DISPLAY`/`XAUTHORITY` no comando de execução.
- Quando você usa `make docker-run`, a pasta atual do projeto é montada dentro do container, então os arquivos baixados e os resultados ficam salvos ali, e não se perdem quando o container é encerrado.
- O Trinity depende do Salmon em tempo de execução. Se aparecer um erro dizendo que o `salmon` não está instalado, o ideal é reconstruir a imagem Docker/Singularity atualizada.
- Avisos do MultiQC sobre arquivos `assets/js/packages/*.js` ausentes podem aparecer em algumas versões empacotadas para Debian — eles não interrompem o pipeline, desde que o log termine com `MultiQC complete`; afetam apenas alguns recursos visuais do relatório HTML.

## Créditos

O Marauders GenoMap foi desenvolvido por Djorkaeff Oliveira, Rodrigo Orvate, João Pedro Lemos e Silva Rodrigues e João Paulo MS Lima, no [EvoMol-Lab](https://evomol-lab.imd.ufrn.br), BioMe, UFRN, Brasil.
