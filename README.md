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