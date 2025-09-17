from src.evaluacion import mejor_equipo_ronda
from src.acumulados import inicializar_acumulados, actualizar_acumulados
from src.resultados import mostrar_tabla

# ----FLUJO PRINCIPAL--------:

## Inicializamos acumulados con los equipos de la primera ronda
acumulados = inicializar_acumulados(list(evaluaciones[0].keys()))

# Procesamos cada ronda
for i, ronda in enumerate(evaluaciones, start=1):
    mejor = mejor_equipo_ronda(ronda)
    acumulados = actualizar_acumulados(acumulados, ronda, mejor[0])
    mostrar_tabla(acumulados, i, mejor)
