"""
    Busca linear em uma lista de contatos para encontrar o número de telefone de um nome específico.
    
    @param nome: Nome do contato a ser buscado.
    @param contatos: Lista de contatos, onde cada contato é um dicionário com 'nome' e 'telefone'.

    @return: Número de telefone do contato ou uma mensagem de erro se o contato não for encontrado.
"""
def buscar_contato(nome, contatos):
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            return f"Número de {nome}: {contato['telefone']}"
    return "Contato não encontrado."

contatos = [
    {"nome": "Alice", "telefone": "1234-5678"},
    {"nome": "Bob", "telefone": "2345-6789"},
    {"nome": "Charlie", "telefone": "3456-7890"}
]

nome_busca = input("Digite o nome do contato que deseja buscar: ")
resultado = buscar_contato(nome_busca, contatos)
print(resultado)
