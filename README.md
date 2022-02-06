# Python 3: Trabalhando com I/O

Curso da Alura sobre Entra e Saída (I/O) no Python

## Objetivo Final &#x1F3AF;

Ler e escrever em um arquivo e falar sobre questões de segurança em arquivos no Python

URL do curso -> [Python 3: Trabalhando com I/O](https://cursos.alura.com.br/course/python-3-trabalhando-com-io)

![Python 3: Trabalhando com I/O](https://www.alura.com.br/assets/api/share/curso-python-3-trabalhando-com-io.png)

## 01 - Lendo Arquivos &#x1F516;
* Como abrir arquivos com o Python.
* O que é o *encoding*.
* Como ler as linhas de um arquivo com os métodos `readline()` e `readlines()`.
* Ler as linhas de um arquivo percorrendo ele através de um *loop*.

### 01 - Entendendo Encoding
* `open(SOURCE)` para abrir um arquivo.
* `.readlines()` para retornar todo o conteúdo de um arquivo.

### 02 - Outras Formas de Leitura
* `.readline()` para ler somente uma linha por vez de um arquivo.
    * `.readline(NUMBER)` para ler somente *x* caracteres do arquivo.
* O ponteiro de leitura do arquivo se move de acordo com as funções utilizadas para ler o arquivo, do início até o final.
* Ler um arquivo utilizando menos memória com a estrutura `for LINE in FILE`.

## 02 - Escrevendo Arquivos &#x1F516;
* Os modos de abertura de um arquivo para escrita.
* Como podemos escrever em um arquivo.
* O momento em que é realizada a escrita do arquivo.
* O comportamento do método `flush()`.
* Como percorrer arquivos com o `seek()`.

### 01 - Começando a Escrever
* A função `file.write(OBJECT)` escreve algo em um arquivo.
* `open(SOURCE, mode="READING_MODE")` para mudar o modo de leitura do arquivo.
    * No modo `"w"`, ele exclui o arquivo original e cria outro.
    * No modo `"a"`, ele insere conteúdo no final do arquivo.

### 02 - Os Métodos Close e Flush
* O **Python** só realiza a escrita no momento que o programa não estiver mais usando o arquivo.
* `.close()` para fechar o arquivo.
* Para indicar que o **Python** deve inserir os dados, mas sem fechar o arquivo, usamos a função `.flush()`.

### 03 - Percorrendo o Arquivo
* `open(FILE, mode="w+")` indica que o arquivo será aberto tanto em modo de escrita como de leitura.
* `.seek(0)` para colocar o ponteiro no início do arquivo.
* O **Python** ignora quebras de linha como o `\n`.
* No modo `a+`, toda operação de `.seek()` é desfeita.

## 03 - Boas Práticas e Exceções &#x1F516;
* A importância de liberar um recurso.
* Como gerenciar contextos utilizando a cláusula `with`.
* Algumas exceções comuns ao se trabalhar com arquivos.
* A diferença dos modos de escrita e de leitura na hora de abrir um arquivo que não existe.

### 01 - Um Pouco de Concorrência
* A boa prática depois de usar um arquivo é sempre fecha-lo.
* Exceções no meio da aberta e fechamento dos arquivos.
* Usar a estrutura `try finally`.

### 02 - Exceções Comuns
* Ao usar o modo de leitura `w` ou `a`, o **Python** cria um arquivo caso ele não exista.

### 03 - Gerenciando o Contexto
* Para trabalhar com um arquivo em um escopo do código usamos `with COMMAND as VARIABLE:`.

## 04 - Conhecendo o Buffer &#x1F516;
* Como funciona a leitura e a escrita de dados por baixo dos panos.
* A classe `bytes`.
* Como funciona o `buffer` de leitura e de escrita.

### 01 - Buffers e Bytes
* Ao ler um arquivo, o **Python** guarda as informações do arquivo no **buffer**, em seguida, ele envia as informações para o programa.
* `b` antes de uma string para transforma-la em um texto em **bytes**.
* Para tranformar uma string em um texto em **bytes** com uma codificação, usamos a função `bytes(TEXT, ENCODING)`.

### 02 - Escrita com o Buffer
* Escrever texto em bytes para um arquivo.

## 05 - Convertendo os Contatos &#x1F516;
* Como utilizar os módulos `csv`, `json`, `pickle`.
* Como serializar e desserializar objetos.
* Como retornar o dicionário de atributos de um objeto.
* Como desempacotar objetos com Python.

### 01 - Do CSV para o Python
* A função `csv.reader()` lê o conteúdo de um arquivo e transforma os dados em uma lista, com posições indexadas. 

### 02 - Convertendo para Pickle
* Um arquivo pickle é um arquivo binário que é entendido pelo **Python**.
* Transformar objetos em dados **Pickle**, que são objetos serializados.
* O parâmetro de leitura `wb`.
* Somente sistemas desenvolvidos em **Python** conseguem desserializar arquivo em formato **pickle**.

### 03 - Convertendo para Json
* Para converter os dados para um arquivo **Json**, usamos a função `json.dump()`.
* A função `__dict__` retorna uma representação do objeto como um dicionário.
* Para converter um arquivo **Json** para dados, usamos a função `json.load()`.
* Desempacotar uma variável no **Python**.