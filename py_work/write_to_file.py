bugs = ["one little bug",2, 1, "another little bug", "java", "where is my cofee", 2]

file = open("little bugs.txt", "r")
file1 = open("2211.txt", "w")
print(file.read())
file1.write(file.read())
file1.close()
file.close()

print("Done.")
