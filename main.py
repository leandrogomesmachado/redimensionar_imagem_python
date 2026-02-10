import os
from datetime import datetime
from PIL import Image
def processar_imagens():
    agora = datetime.now()
    data_formatada = agora.strftime("%d_%m_%Y_%H_%M")
    nome_diretorio = f"out_{data_formatada}"
    if not os.path.exists(nome_diretorio):
        os.makedirs(nome_diretorio)
        print(f"Diretório '{nome_diretorio}' criado com sucesso.")
    extensoes_suportadas = ('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff')
    arquivos = [f for f in os.listdir('.') if f.lower().endswith(extensoes_suportadas)]    
    if not arquivos:
        print("Nenhuma imagem encontrada no diretório atual.")
        return
    print(f"Processando {len(arquivos)} imagens...")
    for arquivo in arquivos:
        try:
            with Image.open(arquivo) as img:
                img_resized = img.resize((36, 36), Image.Resampling.LANCZOS)
                nome_base = os.path.splitext(arquivo)[0]
                caminho_final = os.path.join(nome_diretorio, f"{nome_base}.png")
                img_resized.save(caminho_final, "PNG")
                print(f"  > {arquivo} -> Salvo em {nome_diretorio}")        
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")
    print("\nProcesso concluído!")
if __name__ == "__main__":
    processar_imagens()