def Range(start=0, end=0, step=1) :
    if start > end :
        start, end = end, start
    while start < end :
        yield start
        start += step

for i in Range(10) :
    print(i)

print("menampilkan angka 1-9 secara vertikal")
