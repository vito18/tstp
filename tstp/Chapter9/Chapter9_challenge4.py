import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
movies_jap = [["トップガン", "リスキー・ビジネス", "マイノリティ・リポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレイニング・デイ", ",マン・オン・ファイア", "フライト"]]

with open("movie.csv", "w", encoding="utf-8") as f:
    mov = csv.writer(f, delimiter=",")
    for row in movies:
        mov.writerow(row)

    for row in movies_jap:
        mov.writerow(row)


        
