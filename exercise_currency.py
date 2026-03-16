def currency():
    """
    Ejercicio 13 - Conversión de Moneda

    Dado un monto en pesos argentinos y tasas de cambio, imprimir:
    1. El monto en dólares
    2. El monto en euros
    3. El monto en reales brasileños
    """
    pesos = 10000
    tasa_dolar = 1500  # 1 dólar = 1500 pesos
    tasa_euro = 1600   # 1 euro = 1600 pesos
    tasa_real = 250    # 1 real = 250 pesos

    tasa_dolar_peso = 10000 / 1500
    print(tasa_dolar_peso)

    tasa_euro_peso = 10000 / 1600
    print (tasa_euro_peso)

    tasa_real_peso = 10000 / 250
    print (tasa_real_peso)
