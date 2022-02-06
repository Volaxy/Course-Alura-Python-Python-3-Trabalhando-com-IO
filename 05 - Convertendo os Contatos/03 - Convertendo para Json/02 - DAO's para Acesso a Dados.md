Nos arquivos, criamos um arquivo `util` para realizar a conversão dos dados para JSON e para Pickle.

Pensando em uma abordagem mais orientada a objetos, podemos utilizar um objeto de acesso a dados que fica sendo responsável pela comunicação do mundo Python com o mundo dos arquivos. Este objeto é conhecido como **DAO**, ou Objeto de Acesso a Dados (*Data Access Object*, em inglês).

Quem já trabalhou com banco de dados provavelmente conhece esse padrão de persistência. O DAO é um padrão de projeto muito utilizado por quem busca um meio de acessar seus dados. Popularmente, ele é muito utilizado para acessar o banco de dados e realizar as operações de criação, busca, exclusão e atualização. Além disso, ele pode ser utilizado para salvar e recuperar dados em arquivos, por exemplo.

## Como podemos definir um DAO no projeto?

No nosso caso, queremos ler os contatos de um CSV e salvá-los em dois formatos, pickle e JSON. Pensando em isolar as responsabilidades, podemos definir três DAOs diferentes, um para cada tipo de arquivo. A fim de manter todos os objetos de acesso a dados com as mesmas assinaturas, podemos ainda definir uma classe abstrata que será estendida pelas classes que implementam de fato o acesso a dados.

Para criar uma classe abstrata, precisamos importar do pacote `abc` a classe `ABC` – que será herdada pela classe que padronizará os DAOs – e o *decorator* `abstractmethod` – que será usado para definir os métodos abstratos que serão implementados pelas classes filhas, portanto:
```
from abc import ABC, abstractmethod
```
A classe que definirá as assinaturas das funções se chamará `ContactDao`, e sua definição será parecida com esta:
```
class ContactDao(ABC):

    @abstractmethod
    def find_methods(self, path):
        pass

    @abstractmethod
    def save(self, contacts, path):
        pass
```
Agora, basta definirmos as implementações para essa classe, por exemplo, a classe que salva os dados em JSON pode ficar parecida com esta:
```
class ContatoDaoJSON(ContatoDao):

    @abstractmethod
    def find_all(self, path):
        contacts = []
        with open(path, mode='r') as file:
            contacts_json = json.load(file)
            for contact in contacts_json:
                        c = Contact(**contact)
                        contacts.append(c)

        return contacts   

    @abstractmethod
    def save(self, contacts, path):
        with open(path, mode='w') as file:
    json.dump(contacts, file, default=lambda object: object.__dict__)
```
De uma forma análoga podemos ter as classes `ContactDaoPickle`, `ContactDaoCSV`, `ContactDaoSQL` e as mais diversas implementações da classe `ContactDao`, cada uma isolando a lógica de acesso em seu domínio