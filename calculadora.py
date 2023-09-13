#!/usr/bin/env python
import cgi

# Configura el encabezado HTTP para que el navegador entienda que está recibiendo HTML
print("Content-type: text/html\n")
# HTML para la página web
print("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Calculadora Basica</title>
</head>
<body>
    <h1>Calculadora Basica</h1>
    <form method="post" action="calculadora.py">
        <label for="num1">Numero 1:</label>
        <input type="text" id="num1" name="num1"><br><br>

        <label for="num2">Numero 2:</label>
        <input type="text" id="num2" name="num2"><br><br>

        <label for="operacion">Operacion:</label>
        <select id="operacion" name="operacion">
            <option value="sumar">Sumar</option>
            <option value="restar">Restar</option>
            <option value="multiplicar">Multiplicar</option>
            <option value="dividir">Dividir</option>
        </select><br><br>

        <input type="submit" value="Calcular">
    </form>
""")
# Obtiene los datos del formulario enviado por el usuario
form = cgi.FieldStorage()

# Comprueba si se han enviado los datos del formulario
if "num1" in form and "num2" in form and "operacion" in form:
    num1 = float(form["num1"].value)
    num2 = float(form["num2"].value)
    operacion = form["operacion"].value

    # Realiza la operación correspondiente
    resultado = None
    if operacion == "sumar":
        resultado = num1 + num2
    elif operacion == "restar":
        resultado = num1 - num2
    elif operacion == "multiplicar":
        resultado = num1 * num2
    elif operacion == "dividir":
        if num2 != 0:
            resultado = num1 / num2
print(f"<h2>{resultado}:</h2>")
print(""""
</body>
</html>
      """)

