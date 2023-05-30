class Pessoa:
    """Classe que representa uma pessoa."""
    def __init__(self, nome, idade, endereco, telefone, email):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.hobbies = []

    def get_nome(self):
        """Função para acessar o nome."""
        return self.nome

    def set_nome(self, novo_nome):
        """Função para atualizar nome."""
        self.nome = novo_nome

    def get_idade(self):
        """Função para acessar o idade."""
        return self.idade

    def set_idade(self, nova_idade):
        """Função para atualizar idade."""
        self.idade = nova_idade

    def get_endereco(self):
        """Função para acessar o endereço."""
        return self.endereco

    def set_endereco(self, novo_endereco):
        """Função para atualizar endereço."""
        self.endereco = novo_endereco

    def get_telefone(self):
        """Função para acessar o telefone."""
        return self.telefone

    def set_telefone(self, novo_telefone):
        """Função para atualizar telefone."""
        self.telefone = novo_telefone

    def get_email(self):
        """Função para acessar o email."""
        return self.email

    def set_email(self, novo_email):
        """Função para atualizar email."""
        self.email = novo_email

    def adicionar_hobby(self, hobby):
        """Função que add hobby."""
        self.hobbies.append(hobby)

    def remover_hobby(self, hobby):
        """Função que remove."""
        self.hobbies.remove(hobby)

    def exibir_hobbies(self):
        """Função que exibe hobby."""
        for hobby in self.hobbies:
            print(hobby)
# Criando um objeto da Classe Pessoa
pessoa1 = Pessoa("João", 25, "Rua A, 123","99984311884", "joao@gmail.com")

# Acessando e modificando os atributos do objeto
print(pessoa1.get_nome())  # Saída: João
print(pessoa1.get_idade())  # Saída: 25
print(pessoa1.get_endereco())  # Saída: Rua A, 123
print(pessoa1.get_telefone()) # Saída: 99984311884
print(pessoa1.get_email()) # Saída: joao@gmail.com

pessoa1.set_nome("Carlos")
pessoa1.set_idade(30)
pessoa1.set_endereco("Rua B, 456")
pessoa1.set_telefone("99981158019")
pessoa1.set_email("joao@hotmail.com")

print(pessoa1.get_nome())  # Saída: Carlos
print(pessoa1.get_idade())  # Saída: 30
print(pessoa1.get_endereco())  # Saída: Rua B, 456
print(pessoa1.get_telefone()) # Saída: 99981158019
print(pessoa1.get_email()) # Saída: joao@hmotmailcom
# Adicionando hobbies
pessoa1.adicionar_hobby("Codar")
pessoa1.adicionar_hobby("Fazer Pirâmide")

# Exibindo os hobbies
pessoa1.exibir_hobbies()
# Saída:
# Codar
# Fazer pirâmide