def stars_in_row(n):
    stars = ""
    for i in range(5):
        for t in range(5):
            stars = stars+"*"
        stars = stars+"\n"
    return stars

print(stars_in_row(5))
