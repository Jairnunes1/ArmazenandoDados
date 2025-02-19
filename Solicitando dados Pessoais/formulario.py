nome = input("Insira seu nome: ")
email = input("Insira seu E-mail: ")
telefone = input("Insira seu Telefone: ")

def salvar_arquivo():
   with open("dadosSalvos.txt", "a") as arquivo:
      arquivo.write(f"Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\n")
   print("Dados salvos com sucesso!")

def ler_arquivo(nome_do_arquivo):

   with open(nome_do_arquivo, "r") as arquivo:
      texto = arquivo.read()
      print(texto)


if __name__ == "__main__":
   salvar_arquivo()
   ler_arquivo("dadosSalvos.txt")
