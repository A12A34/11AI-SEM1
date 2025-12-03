import csv  
name = input("Enter your name: ")
with open("PL\\W4-train\\NVxxxxx_W3_D1.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow([name])