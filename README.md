# Windows Spotlight Wallpaper Extractor

Script em Python para extrair automaticamente os wallpapers da tela de bloqueio do Windows Spotlight.

O Windows armazena essas imagens em uma pasta oculta e os arquivos normalmente não possuem extensão.  
Este projeto copia os arquivos da pasta oculta, adiciona a extensão `.jpg` e salva tudo em uma pasta de destino acessível.

---

## Funcionalidades

- Localiza arquivos da pasta oculta do Windows Spotlight
- Copia os arquivos automaticamente
- Adiciona extensão `.jpg`
- Salva em uma pasta de destino
- Evita sobrescrever arquivos existentes
- Automatiza a extração dos wallpapers do Windows

---

## Tecnologias

- Python 3
- `os`
- `shutil`

---

## Como funciona

Arquivos originais do Windows:

```text
a1b2c3d4e5f6
x9y8z7w6v5u4
```

Arquivos gerados:

```text
a1b2c3d4e5f6.jpg
x9y8z7w6v5u4.jpg
```

Caso um arquivo já exista na pasta de destino, o script cria automaticamente:

```text
imagem.jpg
imagem_1.jpg
imagem_2.jpg
```

---

## Caminho padrão do Windows Spotlight

Os wallpapers normalmente ficam armazenados em:

```text
C:\Users\SEU_USUARIO\AppData\Local\Packages\
Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\
LocalState\Assets
```

---

## Como usar

1. Instale o Python 3

2. Configure os caminhos no arquivo Python:

```python
Substitua "SEU_USUARIO" no caminho de origem pelo nome do seu usuário.
origem = r"C:\Users\SEU_USUARIO\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
destino = r"C:\caminho\da\pasta\Destino"
```

3. Execute o script:

```bash
python spotlight_extractor.py
```

---

## Estrutura do Projeto

```text
windows-spotlight-wallpaper-extractor/
│
├── spotlight_extractor.py
├── README.md
└── requirements.txt
```

---

## Objetivo do Projeto

Projeto criado para praticar:

- automação com Python
- manipulação de arquivos
- uso de diretórios e caminhos
- tratamento de arquivos ocultos
- renomeação automática de arquivos
- organização de projetos para GitHub

---

## Observações

Nem todos os arquivos da pasta Assets são imagens válidas.  
Dependendo do sistema, alguns arquivos podem não abrir corretamente.
