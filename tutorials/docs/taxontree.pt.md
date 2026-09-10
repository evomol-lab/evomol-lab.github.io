# Genômica Comparativa - Tutorial 2

# Usando o TaxOnTree

O [**TaxOnTree**](http://bioinfo.icb.ufmg.br/taxontree/) é uma ferramenta de bioinformática, desenvolvida pelos Professores Tetsu Sakamoto (BioMe-UFRN) e José Miguel Ortega (UFMG), projetada para colorir automaticamente árvores filogenéticas com base nas informações taxonômicas do banco de dados NCBI Taxonomy. 

Através da visualização da árvore gerada, a ferramenta permite:

- Identificar a qual espécie cada proteína pertence.
- Verificar o LCA (*Lowest Common Ancestor* - Ancestral Comum Mais Recente) entre a espécie da sua *query* (consulta) e as outras espécies.
- Classificar as proteínas de acordo com a sua classificação taxonômica, como Família, Ordem, Classe, etc.

A saída principal do programa é uma árvore filogenética no formato NEXUS, especialmente configurada para ser visualizada no software [**FigTree**](https://tree.bio.ed.ac.uk/software/figtree/).

---

## Passo a Passo para Submeter uma Análise (*Job*)

O uso pelo site não exige cadastro, permitindo rodar tarefas como um usuário "Convidado" (*guest user*). Caso deseje salvar seu histórico de análises, é possível criar uma conta e fazer login.

### 1. Inserindo os Dados (*Input*)

No painel **"Run TaxOnTree"**, o primeiro passo é escolher o tipo de dado que você fornecerá na aba *Select the type of your input*:

- **Query identifier:** Identificador da proteína (ex: número de acesso do NCBI ou Uniprot).
- **Amino acid sequence:** A sequência de aminoácidos no formato FASTA.
- **List of identifiers:** Uma lista contendo vários identificadores.
- **Tree in Newick:** Uma árvore filogenética já pronta no formato Newick.

Você pode digitar/colar o input na caixa de texto indicada ou fazer o *upload* de um arquivo.

### 2. Configurando Opções da Análise

Abaixo da área de inserção, você pode clicar em **"Options"** para personalizar os parâmetros da busca e alinhamento:

- **BLAST options:** 
  - Escolha a base de dados das sequências (*UniProt Reference proteomes*, *Refseq* fragmentadas ou completas).
  - Defina o limiar (*Threshold %*), *Evalue* e o número máximo de alvos.
- **Alignment options:** Escolha o software de alinhamento múltiplo, como MUSCLE, PRANK, Clustal Omega ou Kalign. Pode-se ativar o "TrimAl" para analisar o alinhamento.
- **Filter options:** Opção útil para excluir isoformas de proteínas ou limitar o número de táxons mostrados em determinada categoria taxonômica (Superreino, Filo, Classe, etc.).
- **Tree options:** Defina o método de enraizamento da árvore: *Midpoint* (ponto médio), *Taxonomic* (busca por folhas taxonomicamente distantes para *outgroup*) ou sem raiz (*No rooting*).

### 3. Submetendo o Job

Dê uma breve descrição para o seu *job* no campo **"Job description"** e clique no botão **"Submit"**. 

> **Guarde o número do seu JobID!** Ele é necessário para buscar os resultados depois.

---

## Como Recuperar e Visualizar seus Resultados

1. Acesse o painel **"*Get your result*"** no site.
2. Insira o seu **JobID**.
3. Selecione o que deseja baixar:
   
   - *Tree in Nexus* (a árvore anotada e colorida).
   
   - *Tree in SVG*.
   
   - *Taxonomy Rep.* (relatório taxonômico).
   
   - *Alignment* (arquivo de alinhamento gerado).
   
   - *Blast result* (resultado da busca BLAST).
4. Clique em ***"Submit"*** para iniciar o download.

### Visualização

Para abrir o arquivo principal da árvore (*Tree in Nexus*), você precisará instalar o software [**FigTree**](https://tree.bio.ed.ac.uk/software/figtree/) no seu computador (o link de download está disponível no próprio site do [TaxOnTree](http://bioinfo.icb.ufmg.br/taxontree/)). O formato de nomenclatura das folhas (*leaf names*) exibido na árvore gerada geralmente traz o ID primário, nome do gene e o nome da espécie, facilitando a interpretação das cores e grupos taxonômicos (ex: *P00156 CYTB Homo sapiens*).

---

## Versão de Linha de Comando e Código Aberto

Se for trabalhar com análise em larga escala, o TaxOnTree também oferece uma versão de linha de comando para ambientes UNIX. O código-fonte (*Source*) pode ser baixado do repositório da ferramenta no [GitHub](https://github.com/tetsufmbio/taxontree), e permite a customização de bancos de dados locais para o BLAST.

## Tutorial avançado

O próprio autor, Prof. Tetsu Sakamoto disponibilizou um tutorial para a utilização da ferramenta, que pode ser obtido [AQUI](Material_taxontree.pdf), ***apenas para fins didáticos***. <span style="color:red">**A reprodução dele para qualquer outro fim não é permitida e nem consentida.**</span>

---

## TaxOnTree Citation

Para citar qualquer análise com o TaxOnTree, use o [preprint](https://www.biorxiv.org/content/10.1101/2020.12.24.424364v1):

```
@article {Sakamoto2020.12.24.424364,
	author = {Sakamoto, Tetsu and Ortega, J. Miguel},
	title = {TaxOnTree: a tool that generates trees annotated with taxonomic information},
	elocation-id = {2020.12.24.424364},
	year = {2020},
	doi = {10.1101/2020.12.24.424364},
	publisher = {Cold Spring Harbor Laboratory},
	URL = {https://www.biorxiv.org/content/early/2020/12/24/2020.12.24.424364},
	eprint = {https://www.biorxiv.org/content/early/2020/12/24/2020.12.24.424364.full.pdf},
	journal = {bioRxiv}
}
```