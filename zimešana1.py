import turtle

t = turtle.Turtle()  # Izveidojam bruņurupuci
t.shape("turtle")    # Piešķiram tam bruņurupuča izskatu
t.color("green")     # Nomainām krāsu

# Pamata kustības
for x in range(4):
    t.forward(100)       # Uz priekšu par 100 pikseļiem
    t.left(90)           # Pagrieziens pa kreisi par 90 grādiem

turtle.done()        # Logu neaizvērt uzreiz