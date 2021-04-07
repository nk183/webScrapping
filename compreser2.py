from PIL import Image
import math

foo = Image.open("C:\\Users\\nk\\Pictures\\namandocphotos\\naman.jpeg")
x, y = foo.size
x2, y2 = math.floor(x-50), math.floor(y-20)
foo = foo.resize((x2,y2),Image.ANTIALIAS)
foo.save("C:\\Users\\nk\\Pictures\\namandocphotos\\naman1.jpeg",quality=50)