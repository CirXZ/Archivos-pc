import pyautogui as py

pos = py.position()
print(pos)

# py.moveTo(300,200)

pregunta = input("Estas Triste?: ")
if pregunta.lower() == "si":
    print("\U0001F97A")
    
else:
    print("\U0001F600")
