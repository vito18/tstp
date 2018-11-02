import csv

movies = [["Top Gun", "Risky Business", "Minority"], ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w") as f:
    mov = csv.writer(f, delimiter=",")
    for row in movies:
        mov.writerow(row)

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies2.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
