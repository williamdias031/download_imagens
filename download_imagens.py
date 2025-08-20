import os
import requests

def baixar_imagens(urls, pasta="imagens"):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    for i, url in enumerate(urls, start=1):
        try:
            print(f"🔗 Baixando imagem {i}: {url}")
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()

            # Tenta pegar a extensão do arquivo
            ext = url.split(".")[-1].split("?")[0]
            if ext.lower() not in ["jpg", "jpeg", "png", "gif", "bmp", "webp"]:
                ext = "jpg"

            caminho_arquivo = os.path.join(pasta, f"imagem_{i}.{ext}")

            with open(caminho_arquivo, "wb") as f:
                f.write(resposta.content)

            print(f"✅ Imagem salva em: {caminho_arquivo}")

        except Exception as e:
            print(f"❌ Erro ao baixar {url}: {e}")


def main():
    print("=== Downloader de Imagens ===")
    print("Digite as URLs (uma por linha).")
    print("Quando terminar, pressione ENTER em uma linha vazia.\n")

    urls = []
    while True:
        url = input("URL: ").strip()
        if not url:
            break
        urls.append(url)

    if urls:
        baixar_imagens(urls)
    else:
        print("⚠️ Nenhuma URL fornecida.")


if __name__ == "__main__":
    main()
