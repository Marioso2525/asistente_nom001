class CalculadorConductores:
    """Cálculos basados en la NOM-001-SEDE-2012 (Tabla 310-16)"""

    @staticmethod
    def calcular_calibre(amperios, material="cobre", temperatura=75):
        """
        Determina calibre mínimo según corriente (valores de ejemplo).
        Reemplazar con datos reales de la norma.
        """
        tabla = {
            "cobre": {
                75: {
                    15: "14 AWG",
                    20: "12 AWG",
                    30: "10 AWG",
                    55: "8 AWG",
                    70: "6 AWG",
                    85: "4 AWG",
                    95: "3 AWG",
                    110: "2 AWG",
                }
            }
        }
        try:
            for amp_max, calibre in tabla[material][temperatura].items():
                if amperios <= amp_max:
                    return calibre
            return "Calibre superior requerido (consultar tabla completa)"
        except KeyError:
            return "Combinación no disponible"

    @staticmethod
    def factor_correccion_temperatura(temp_ambiente, temp_base=30):
        """Factores de corrección por temperatura (valores ilustrativos)"""
        factores = {
            25: 1.05,
            30: 1.00,
            35: 0.94,
            40: 0.88,
            45: 0.82,
        }
        return factores.get(temp_ambiente, 0.82)
