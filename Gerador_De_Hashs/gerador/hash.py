import hashlib

def GeradorDeHash(arquivoNome):
  hashMd5 = hashlib.md5()

  with open(arquivoNome, "rb") as arquivo:
    carregarArquivo = 0
    while(carregarArquivo != b''):
      carregarArquivo = arquivo.read(1024)
      hashMd5.update(carregarArquivo)
  arquivoHash = hashMd5.hexdigest()

  return arquivoHash