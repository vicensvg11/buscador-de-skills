"""Puntuación ponderada de la Fase 1.4. Uso: python3 scoring.py"""
import csv

PESOS = {"canal": .20, "demanda": .15, "pago": .15, "automat": .10, "tiempo": .10,
         "economia": .10, "anti_ia": .10, "diferenc": .05, "riesgo_inv": .05}

with open("scoring.csv", encoding="utf-8") as f:
    filas = [(r["idea"], sum(float(r[k]) * w for k, w in PESOS.items())) for r in csv.DictReader(f)]
for i, (idea, total) in enumerate(sorted(filas, key=lambda x: -x[1]), 1):
    print(f"{i}. {total:.2f}  {idea}")
