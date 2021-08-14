a, b, c = map(float, input().split())

triangle = a * c / 2
circle = 3.14159 * (c ** 2) 
trapeze = (a + b) * c / 2
square = b ** 2
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapeze:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
