from pathlib import Path
from time import perf_counter

PASTA = Path(__file__).resolve().parent
ARQUIVO_ENTRADA = PASTA / "texto.txt"
ARQUIVO_SAIDA = PASTA / "palavras_ordenadas.txt"


def bubble_sort(palavras):
    itens = palavras.copy()
    for limite in range(len(itens) - 1, 0, -1):
        houve_troca = False
        for i in range(limite):
            if itens[i].casefold() > itens[i + 1].casefold():
                itens[i], itens[i + 1] = itens[i + 1], itens[i]
                houve_troca = True
        if not houve_troca:
            break
    return itens


def selection_sort(palavras):
    itens = palavras.copy()
    for inicio in range(len(itens) - 1):
        menor = inicio
        for i in range(inicio + 1, len(itens)):
            if itens[i].casefold() < itens[menor].casefold():
                menor = i
        if menor != inicio:
            itens[inicio], itens[menor] = itens[menor], itens[inicio]
    return itens


def medir(nome, funcao, palavras):
    inicio = perf_counter()
    resultado = funcao(palavras)
    segundos = perf_counter() - inicio
    print(f"{nome}: {segundos:.6f} segundos")
    return nome, resultado, segundos


def main():
    if not ARQUIVO_ENTRADA.exists():
        raise FileNotFoundError(
            f"Não encontrei {ARQUIVO_ENTRADA.name}. Coloque-o na mesma pasta de kdd.py."
        )

    palavras = []
    with ARQUIVO_ENTRADA.open("r", encoding="utf-8-sig") as arquivo:
        for linha in arquivo:
            palavras.extend(linha.split())

    if not palavras:
        print("O arquivo texto.txt não contém palavras.")
        ARQUIVO_SAIDA.write_text("", encoding="utf-8")
        return

    print(f"Total de palavras: {len(palavras)}")
    resultados = [
        medir("Bubble Sort", bubble_sort, palavras),
        medir("Selection Sort", selection_sort, palavras),
        medir("sort() nativo", lambda lista: sorted(lista, key=str.casefold), palavras),
    ]

    metodo, ordenadas, segundos = min(resultados, key=lambda item: item[2])
    print(f"Método mais rápido nesta execução: {metodo} ({segundos:.6f} s)")
    print("Palavras ordenadas:")
    print(" ".join(ordenadas))

    ARQUIVO_SAIDA.write_text(" ".join(ordenadas) + "\n", encoding="utf-8")
    print(f"Resultado salvo em: {ARQUIVO_SAIDA.name}")


if __name__ == "__main__":
    main()
