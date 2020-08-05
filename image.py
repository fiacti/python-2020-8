
f_copy = open("trump.jpg", "rb")
img = f_copy.read()
print(img)
f_copy.close()

copy = open('copy.jpg','wb')
copy.write(img)
copy.close()