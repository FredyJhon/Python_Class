'''
Una familia decide organizar una reunión para 45 personas en una finca. 
El alquiler del lugar cuesta $1.200.000 e incluye 30 sillas y 5 mesas. 
Cada silla adicional cuesta $3.000 y cada mesa adicional $25.000. 
Se calcula que por cada mesa se pueden sentar 6 personas cómodamente. 
Además, el servicio de comida tiene un costo de $28.000 por adulto y $18.000 por niño.
Se estima que asistirán 30 adultos y el resto serán niños. 
La familia quiere cobrar una cuota equitativa solo a los adultos para cubrir todos los gastos. 
¿Cuánto debe pagar cada adulto si también se incluye un 10% adicional para imprevistos? este es el anunciado

'''
import math

personas = 45
adultos = 30
alquiler = 1200000
sillas_incluidas = 30
mesas_incluidas = 5

#Precios
valor_silla_adicional = 3000
valor_mesa_adicional = 25000
comida_adulto = 28000
comida_nino = 18000
imprevisto = 0.10

ninos = personas - adultos

sillas_faltantes = personas - sillas_incluidas

mesas_totales_necesarias = math.ceil(personas /6)
mesas_faltantes = mesas_totales_necesarias - mesas_incluidas


costo_sillas = sillas_faltantes * valor_silla_adicional
costo_mesas = mesas_faltantes * valor_mesa_adicional
costo_comida_adulto = adultos * comida_adulto
costo_comida_ninos = ninos * comida_nino

subtotal = alquiler + costo_sillas + costo_mesas +costo_comida_adulto + costo_comida_ninos
total_imprevisto = subtotal * imprevisto
total_general = subtotal + total_imprevisto

pago_total_adulto = (total_general / adultos)

print(f"La cuota a pagar por adulto es : ${pago_total_adulto:.0f}")


