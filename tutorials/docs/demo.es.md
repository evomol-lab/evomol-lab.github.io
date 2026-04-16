# Representación computacional de Biomoléculas

El objetivo de este tutorial es introducir conceptos relacionados con la representación y visualización computacional de moléculas biológicas, como proteínas, ácidos nucleicos, ligandos pequeños, etc. Sirve como soporte visual para la comprensión de las estructuras tridimensionales y las uniones/interacciones químicas que las estabilizan.

**Observaciones:**

- Este tutorial fue construido ***solo para fines didácticos***. <span style="color:red">**La reproducción del mismo para cualquier otro fin no está permitida ni consentida.**</span>
- Para optimizar el tiempo, las herramientas/programas utilizados aquí ya deben estar instalados en la máquina. Navegue por el resto del sitio para verificar los pasos necesarios para su instalación.

***Vea también el tutorial comentado en audio (generado automáticamente por Inteligencia Artificial):***

<iframe
  src="https://drive.google.com/file/d/1NJhVgb-8Oo6rEI7woKalrN03GtbCpZyM/preview"
  width="300"
  height="60"
  frameborder="0"
  allow="autoplay; encrypted-media"
  allowfullscreen
></iframe>

**ATENCIÓN**

<span style="color:red">El audio anterior es solo para ayudar en la accesibilidad; no narra todos los pasos. Escucharlo no sustituye la ejecución de las etapas siguientes ni reemplaza las clases presenciales con el profesor/instructor.</span>

## Nociones Básicas de Visualización computacional de moléculas

### Ácidos Nucleicos

Los ácidos nucleicos son moléculas informacionales con una estructura tridimensional. Esta es uniforme en el caso de la doble hélice (ADN o ARN) o variable en el caso de ARNs con estructuras secundarias/terciarias biológicamente activas. La información puede representarse en forma de caracteres simples, como un archivo de texto (texto plano, no en un .doc). La forma más común de representación de información de secuencias de nucleótidos o proteínas en Bioinformática es el formato **fasta**. Fue desarrollado por David J. Lipman y William R. Pearson en 1985, junto con un programa de búsqueda de similitudes de secuencias llamado [FASTA](https://pubmed.ncbi.nlm.nih.gov/2983426/), que fue reemplazado en muchas aplicaciones posteriormente por el [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi).

Comienza con una línea de descripción precedida por `>`, seguida de la secuencia propiamente dicha, sin espacios ni números. Su simplicidad facilita la manipulación y el análisis de datos biológicos. A continuación se muestra un ejemplo de una secuencia nucleotídica en este formato:

```fasta
>Secuencia_1
TCTCGATGCAGCTAGCTATCGCAT
```
En las líneas relativas a la secuencia, solo se aceptan los caracteres canónicos para nucleótidos y aminoácidos, que pueden consultarse [AQUÍ](https://web.archive.org/web/20110811073845/http://www.dna.affrc.go.jp/misc/MPsrch/InfoIUPAC.html).

Copie la secuencia de arriba y péguela en un documento de texto simple (usando el Bloc de notas o gedit, en SO Windows y Linux, respectivamente).

#### Transformando en visualización tridimensional

Para transformar la visualización de esta información en una estructura tridimensional, utilizaremos el programa [UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/) y seguiremos estos pasos:

- Abra ChimeraX.
- Al abrir el programa, debería aparecer una pantalla similar a la siguiente:

![Página Inicial de UCSF ChimeraX](demo0.png)

>*Si aparece una pantalla negra, haga clic en el icono marcado en la figura anterior.*

- Siga ahora esta ruta en el menú:
  - *Tools... Structure Editing... Build Structure*

![Menú de construcción de moléculas](demo1.png)

- En la pestaña lateral aparecerá un cuadro de diálogo. Haga clic en *helical DNA/RNA* y pegue la secuencia descrita anteriormente en el cuadro, manteniendo marcadas las opciones *DNA* y *B-Form*, según la figura siguiente:

![Menú de construcción de moléculas](demo2.png)

- Haga clic en `Apply`. Su molécula debería aparecer.

![Menú de construcción de moléculas](demo3.png)

- Explore la molécula y sus diferentes representaciones haciendo clic en la pestaña superior *Molecule Display*. Estos pasos serán dirigidos por el profesor durante la demostración.

>*También puede usar su propia secuencia o cambiar la forma de visualización. Por ejemplo, ¿qué tal hacer una doble hélice híbrida ADN/ARN?*

- Vamos a guardar la molécula en otro formato de archivo llamado `pdb`.
  - Vaya a *File* > *Save...* y guarde la molécula con el nombre `Seq1.pdb`.
- Ahora abriremos ese archivo en un editor de texto.
- ¿Verificamos su formato?

## Representando moléculas pequeñas

Vamos a utilizar ahora una notación química simplificada, llamada SMILES (*Simplified Molecular Input Line Entry System*), que sirve para la representación de moléculas y reacciones.

> *Más información sobre SMILES se puede encontrar [AQUÍ](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html).*

A partir del sitio de información sobre [SMILES](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html) o mediante búsquedas en Google o bases de datos de estructuras químicas (como [PubChem](https://pubchem.ncbi.nlm.nih.gov)), busque por nombre y dibuje otras moléculas de su interés. Por ejemplo, ¿visualizamos la estructura de la Rosuvastatina [Haga clic aquí](https://pubchem.ncbi.nlm.nih.gov/compound/446157)?

- En la página de información del fármaco, busque el código SMILES, que estará en el campo "*Canonical SMILES*":

```
CC(C)C1=NC(=NC(=C1/C=C/[C@H](C[C@H](CC(=O)O)O)O)C2=CC=C(C=C2)F)N(C)S(=O)(=O)C
```
- Este código SMILES se puede utilizar para construir la molécula en el cuadro de diálogo ```Build Structure``` de UCSF Chimera.

El código de la molécula de Rosuvastatina en PubChem es 446157. En *File > Fetch by ID*, marque la base de datos PubChem e introduzca este código.

- Observe la representación de la Rosuvastatina en los diferentes tipos de visualización. Vea qué otras moléculas le interesan.

### Proteínas

Las proteínas también son moléculas informacionales, sin embargo, con un "alfabeto" mayor, de 20 aminoácidos proteicos (codificados en el código genético), descritos en la figura siguiente:

![Clasificación de los Aminoácidos basada en las características químicas del grupo R](str1-fig5.png)

La tabla siguiente resume los códigos de 1 y de 3 letras de estos aminoácidos:

| Aminoácido | Código de 3 letras | Código de 1 Letra |
|:-------|:--:|:--:|
| Alanina | Ala | A |
| Arginina | Arg | R |
| Asparagina | Asn | N |
| Aspartato | Asp | D |
| Cisteína | Cys | C |
| Glutamato | Glu | E |
| Glutamina | Gln | Q |
| Glicina | Gly | G |
| Histidina | His | H |
| Isoleucina | Ile | I |
| Leucina | Leu | L |
| Lisina | Lys | K |
| Metionina | Met | M |
| Fenilalanina | Phe | F |
| Prolina | Pro | P |
| Serina | Ser | S |
| Treonina | Thr | T |
| Triptófano | Trp | W |
| Tirosina | Tyr | Y |
| Valina | Val | V |

En otro momento, podrá ver la fórmula individual de todos estos aminoácidos usando el menú ```Build Structure``` de UCSF Chimera, haciendo clic en peptide e introduciendo solo un aminoácido, utilizando siempre el código de una letra.

La información de la estructura primaria de las proteínas también se describe en formato `fasta`:

```
>Pep1
RDQ
```
### Verificando ángulos de rotación

Ahora trabajaremos con el péptido anterior (RDQ) para visualizar las diferentes posibilidades de los ángulos de rotación **ø** (*phi*) y **Ψ** (*psi*), y relacionarlos con el [Gráfico de Ramachandran](https://en.wikibooks.org/wiki/Structural_Biochemistry/Proteins/Ramachandran_Plot). Para ello, siga estos pasos:

- *Tools... Structure Editing... Build Structure*

En la ventana que aparezca, haga clic en ```peptide``` y en el espacio indicado introduzca **RDQ**.

![Construyendo un péptido](demo4.png)

- En el campo ```named```, asigne un nombre a la molécula o deje el predeterminado.
- Haga clic en `Apply`.

En la ventana que se abra a continuación, verifique los ángulos **ø** (*phi*) y **Ψ** (*psi*) asignados por defecto en el residuo D (-57/-47). Haga clic nuevamente en `Apply`, pero en este caso deje esta ventana abierta. Aparecerá la primera molécula.

![Ángulos phi y psi](demo5.png)

En esta misma ventana, cambiará los ángulos de rotación de la siguiente forma:
- Seleccionará el residuo D y en las casillas inferiores pondrá 0 grados para ambos ángulos *ø* y *Ψ*. Presione la tecla ```Set```, verifique si los ángulos relativos al residuo D cambiaron y haga clic en `Apply`.

![Ajustando los ángulos de torsión](demo6.png)

- Añada los átomos de H para las 3 moléculas según lo mostrado en clase (*Tools > Structure Editing > Add Hydrogens*). Cambie también las opciones de visualización a su visualización favorita.

Las dos moléculas aparecerán superpuestas. Haga clic en la pestaña `Right Mouse` en la ventana principal de ChimeraX, haga clic en *Drag Model* y con el puntero del ratón sobre uno de los péptidos, haga clic con el botón derecho y arrástrelo a otro lugar de la pantalla para evitar la superposición.

![Péptidos RDQ](demo7.png)

Verifique las superposiciones entre los átomos causadas por los diferentes ángulos de torsión alrededor del enlace peptídico del residuo D.

### Estructuras secundarias

Ahora abriremos una primera estructura completa.

- Haga clic en *File > Fetch by ID*.
- En la ventana que aparece, seleccione la base de datos ```PDB``` y en el campo escriba [1ZIK](https://www.rcsb.org/structure/1ZIK).

![Descargando estructuras](demo8.png)

- Haga clic en `Fetch`.
- Mueva y observe las características de esta estructura.

Esta proteína es una cremallera de leucina formada por dos péptidos.

> *¿Cuál es el tipo de estructura secundaria principal de esta proteína?*

La visualización inicial predeterminada es en cintas (ribbons). Para mostrar también sus átomos, haga clic en:

- *Actions... Atoms/Bonds... show*.

El comando muestra todos los átomos y enlaces de la estructura, excepto aquellos que en la cadena del péptido son suprimidos por la visualización de la cinta. Inicialmente, los heteroátomos (átomos distintos al carbono) están codificados por colores según el elemento: oxígeno rojo, nitrógeno azul, etc. Los carbonos conservan el color del modelo.

- Intente mover la estructura con el ratón en la ventana principal de gráficos.

Ahora retiremos la visualización en cintas:

- *Actions... Ribbon... hide* (Para mostrar solo los átomos).

Identifique los aminoácidos, sus cadenas laterales y los enlaces peptídicos.

Ahora seleccione una de las cadenas de la estructura 1ZIK y muestre los puentes de hidrógeno con la opción:

- *Tools... Structure Analysis... H-Bonds*. En la ventana que se abre a continuación, haga clic en `Ok`.

Observe los puentes de hidrógeno que estabilizan la estructura de las alfa-hélices.

>*En ChimeraX, todos los comandos anteriores pueden realizarse haciendo clic en los iconos.*

Analicemos ahora una estructura que también tenga hojas beta.

- Haga clic en *File > Fetch by ID*.
- In the window that appears, seleccione la base de datos ```PDB``` y en el campo escriba [5BVL](https://www.rcsb.org/structure/5BVL).
- Haga clic en `Fetch`.
- Mueva y observe las características de esta estructura.

Vamos a visualizar de forma diferenciada los tipos de estructura secundaria en esta estructura:

- Vaya a la línea de comandos, en la parte inferior de ChimeraX, escriba *color strand red* y presione `ENTER`. Las hojas beta deberían aparecer ahora en rojo.

### Estructuras Terciaria y Cuaternaria

La estructura primaria de la insulina se representa en la figura siguiente:

![Estructura Primaria de la Insulina](str1-fig15.png)

Ahora trabajaremos con la estructura terciaria de esta hormona. Abra de la forma indicada anteriormente la estructura [1ZEH](https://www.rcsb.org/structure/1ZEH).

Con ella abierta, identifique:

- Las cadenas de la hormona insulina.
- Los tipos de estructuras secundarias involucradas.
- Obtenga el gráfico de Ramachandran.
- Visualice los puentes de H.
- Localice y visualice los puentes disulfuro (S-S).
> *Para este último ítem, el consejo es buscar las cisteínas, según la figura siguiente.*

Para verificar estructuras cuaternarias, descargaremos la estructura de la HMG-CoA Sintasa Humana en complejo con la Rosuvastatina. Esta estructura es el PDB [1HWL](https://www.rcsb.org/structure/1HWL). Siga los pasos orientados en clase.

## Predicción del efecto de modificaciones

A partir del número de acceso [Uniprot](http://uniprot.org) (o del entry name) de la proteína obtendremos información sobre el modelado computacional automático de esa proteína y sobre la predicción funcional de modificaciones de su secuencia a partir de [AlphaMissense](https://deepmind.google/discover/blog/a-catalogue-of-genetic-mutations-to-help-pinpoint-the-cause-of-diseases/). El número de acceso Uniprot que utilizaremos es [P04035 · HMDH_HUMAN](https://www.uniprot.org/uniprotkb/P04035/entry). Haga clic en ese registro para verificar la descripción de esta proteína.

- Abra la página de [AlphaFoldDB](https://alphafold.ebi.ac.uk/).
- En el campo de búsqueda, introduzca el número de acceso Uniprot o su entry name y haga clic en `SEARCH`.
- Haga clic en el resultado obtenido o puede ir directamente [AQUÍ](https://alphafold.ebi.ac.uk/entry/P04035).

En el registro de AlphaFoldDB, verá la estructura tridimensional modelada y justo debajo verá un gráfico con la predicción de impacto funcional realizada por [AlphaMissense](https://deepmind.google/discover/blog/a-catalogue-of-genetic-mutations-to-help-pinpoint-the-cause-of-diseases/). Cada modificación prevista (cambio de un aminoácido por cualquiera de los otros 19) en cada sitio de la secuencia primaria puede observarse en el gráfico, que describe el resultado en tres categorías: Benignas (Azules), Probablemente Patogénicas (Rojas) y Efecto incierto (Gradiente entre azul e rojo). Esta escala refleja la puntuación AlphaMissense (*am_score*), que varía entre 0 (más benigna) hasta 1 (más patogénica).

## COSMIC-3D

El [COSMIC-3D](https://cancer.sanger.ac.uk/cosmic3d/) es una base de datos que integra mutaciones asociadas al cáncer con estructuras tridimensionales del proteoma humano. Es una base muy interesante para visualizar el efecto de mutaciones/polimorfismos en la estructura de las proteínas.

![Cosmic-3D](dbsnp-cosmic3d-1.png)

### Ejemplo de uso:

Utilizaremos el gen FGFR2, introduciendo su sigla (en realidad, su GeneSymbol) en el campo de búsqueda. Justo debajo aparece un cuadro con el código Uniprot de la proteína y el número de estructuras disponibles. Presione `ENTER`.

En la página siguiente verá la estructura de la proteína y un gráfico que resume las mutaciones reportadas, su cobertura estructural y su frecuencia de aparición. Al hacer clic en la mutación, el cambio de aminoácido se visualiza en la estructura.

- ¿Cuál es el impacto de una mutación en la posición 376 de esta proteína?
- ¿Posee cobertura estructural?

El video a continuación demuestra la búsqueda del gen EGFR:

<iframe src="https://drive.google.com/file/d/1pFc1kVYLBHkjd4zQZOcx61kXjuIapBVP/preview" width="640" height="480" allow="autoplay"></iframe>