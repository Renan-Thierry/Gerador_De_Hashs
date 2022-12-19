import rsa;
import tarfile;
from gerador.hash import GeradorDeHash;

def escreverMensagem():
  mensagem = input("Digite sua mensagem: ")
  print(b)
  with open('arquivo.txt', 'w') as arquivo:   
        for valor in mensagem:
          arquivo.write(str(valor))
          print("\nmensagem escrita no arquivo!!!\n")
        print(b)

def gerarChaves():
  chavePublica, chavePrivada = rsa.newkeys(1024) 
  with open("./Chaves/ChavePublica.pem", "wb") as arquivo: 
    arquivo.write(chavePublica.save_pkcs1("PEM"))

  with open("./Chaves/ChavePrivada.pem", "wb") as arquivo: 
    arquivo.write(chavePrivada.save_pkcs1("PEM"))
  print("\nConjunto de chaves gerados\n")
  print(b)
  
def descompactarArquivo():
  arquivoCompactado = tarfile.open("arquivos.tar", "r")
  arquivoCompactado.extractall("arquivos") 
  arquivoCompactado.close()
  print("\nO arquivo foi Descompactado\n")
  print(b)
  
def compararHash():
  hashDoArquivoTxt = GeradorDeHash("./arquivos/arquivo.txt")

  with open("./Chaves/ChavePrivada.pem", "rb") as arquivo:
    chavePrivada = rsa.PrivateKey.load_pkcs1(arquivo.read())
  
  with open("./arquivos/arquivoHashEncriptado.txt", "rb") as arquivo:
    arquivoHash = arquivo.read()
    arquivoHashDesencriptado = rsa.decrypt(arquivoHash, chavePrivada) 
    arquivoHashDesencriptado = arquivoHashDesencriptado.decode()
  if (hashDoArquivoTxt == arquivoHashDesencriptado): 
      print("\nAs chaves são iguais, o arquivo e totalmente autêntico\n")
      print(b)
  else:
      print("As chaves não são iguais, o arquivo não e autêntico\n")
      print(b)

while True:
  a = "=-" * 15
  b = "=-" * 36

  print("\n" + a + "Criptografia" + a + "\n")
  print("1 - Escrever Mensagem")
  print("2 - Gerar conjunto de chaves")
  print("5 - Descompactar arquivo")
  print("6 - Descriptografar hash e Comparar")
  print("0 - Sair\n")
  print(b)

  opção = int(input("Escolha sua opção: "))

  if opção == 1:
    escreverMensagem()

  elif opção == 2:
    gerarChaves()

  elif opção == 5:
    descompactarArquivo()

  elif opção == 6:
    compararHash()

  elif opção == 0:
    exit()
  
  else:
    print("\nEssa opção não e valida, tente novamente\n")
    print(b)