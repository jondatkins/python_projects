import pyinputplus as pyip

while True:
    prompt = "¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n"
    response = pyip.inputYesNo(prompt, yesVal="sí", noVal="no")
    if response == "no":
        break
