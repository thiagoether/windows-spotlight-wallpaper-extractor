import shutil
import os

arquivos_copiados = 0

origem = r"C:\Users\Thiago Ether\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
destino = r"C:\lockscreen_img"

os.makedirs(destino, exist_ok=True)

for arquivo in os.listdir(origem):
    caminho_origem = os.path.join(origem, arquivo)    

    if os.path.isfile(caminho_origem):
        novo_nome = arquivo + ".jpg"
        caminho_destino = os.path.join(destino, novo_nome)
        
        if not os.path.exists(caminho_destino):
            shutil.copy2(caminho_origem, caminho_destino)
            arquivos_copiados += 1
            # print(f"Copiado: {arquivo}")
        else:
            print(f'Já existe {novo_nome}')

# print(f'{len(os.listdir(origem))} arquivos copiados.')
print(f'{arquivos_copiados} arquivos copiados')


print("Concluído!")