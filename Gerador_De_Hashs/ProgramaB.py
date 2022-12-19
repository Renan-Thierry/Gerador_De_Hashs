import rsa;
import tarfile;
from gerador.hash import GeradorDeHash;

with open("./Chaves/ChavePublica.pem", "rb") as arquivo:
  chavePublica = rsa.PublicKey.load_pkcs1(arquivo.read())

def gerarHashDoArquivo():
  hash = GeradorDeHash("arquivo.txt") 
  arquivoHashEncriptado = rsa.encrypt(hash.encode(), chavePublica) 
  with open("arquivoHashEncriptado.txt", "wb") as arquivo: 
    arquivo.write(arquivoHashEncriptado)
  print("\nO hash do arquivo foi criado e encriptado com Sucesso\n")
  print(b)

def ArquivoCompactado():
  arquivoCompactado = tarfile.open("arquivos.tar", "w") 
  arquivoCompactado.add("arquivo.txt") 
  arquivoCompactado.add("arquivoHashEncriptado.txt") 
  arquivoCompactado.close() 
  print("\nO arquivo foi Encriptado\n")
  print(b)


while True:
  a = "=-" * 15
  b = "=-" * 36

  print("\n" + a + "Criptografia" + a + "\n")
  print("3 - Gerar hash do arquivo e encriptar")
  print("4 - criar arquivo compactado")
  print("0 - Sair\n")
  print(b)

  opção = int(input("Escolha sua opção: "))

  if opção == 3:
    gerarHashDoArquivo()

  elif opção == 4:
    ArquivoCompactado()

  elif opção == 0:
    exit()

  else:
    print("\nEssa opção não e valida, tente novamente\n")
    print(b)