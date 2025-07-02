def create_dominoes():
    dominoes = []
    for i in range(7):  # 0'dan 6'ya kadar sayılar
        for j in range(i, 7):  # i'den 6'ya kadar sayılar
            dominoes.append((i, j))
    return dominoes

# Ana program
if __name__ == "__main__":
    dominoes = create_dominoes()

    # Tüm domino taşlarını yazdırma
    print("Domino taşlarının tüm olasılıkları:")
    for domino in dominoes:
        print(domino)
