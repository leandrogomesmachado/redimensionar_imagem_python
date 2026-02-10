# Image Resizer Automático 

Este script Python automatiza o redimensionamento de imagens em lote. Ele busca todas as imagens no diretório atual, redimensiona-as para **36x36 pixels** e as organiza em uma nova pasta datada para manter o seu diretório original limpo.

##  Funcionalidades

* **Detecção Automática:** Identifica arquivos `.jpg`, `.jpeg`, `.png`, `.bmp`, `.webp` e `.tiff`.
* **Organização Inteligente:** Cria uma pasta de saída com timestamp (ex: `out_10_02_2026_08_30`).
* **Alta Qualidade:** Utiliza o filtro `LANCZOS` para garantir nitidez mesmo em tamanhos pequenos.
* **Padronização:** Converte todas as imagens processadas para o formato `.png`.

## 🛠️ Pré-requisitos

O script utiliza a biblioteca **Pillow** para o processamento de imagens.

1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca necessária via terminal:

```bash
pip install Pillow
```
## Como Usar

* Coloque o script na mesma pasta das imagens que deseja redimensionar.

* Execute o script:
  ```bash
  python nome_do_seu_arquivo.py
  ```

  Estrutura de Saída
O script processa os arquivos e os organiza da seguinte forma:

Entrada: foto_original.jpg (Qualquer tamanho)

Saída: out_DD_MM_AAAA_HH_MM/foto_original.png (36x36 pixels)
