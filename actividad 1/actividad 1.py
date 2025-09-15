# version corregida - más robusta
try:
    import sympy as sp
except ImportError:
    print("Error: 'sympy' no está instalado. Instálalo con: pip install sympy")
    raise

class Funcion:
    def __init__(self):
        self.expresion = None          # expresión sympy
        self.variables = []            # lista de sympy.Symbol (ordenada por nombre)
        self.restricciones = []        # lista de objetos sympy (Relational u otros)

    def ingresar_funcion(self):
        while True:
            funcion_str = input("Ingrese la función (ejemplo: x**2 + y - z): ").strip()
            if not funcion_str:
                print("No ingresaste nada. Intenta de nuevo.")
                continue
            try:
                expr = sp.sympify(funcion_str)
                self.expresion = expr
                # ordenar variables por nombre para consistencia
                syms_sorted = sorted(list(expr.free_symbols), key=lambda s: s.name)
                self.variables = syms_sorted
                break
            except Exception as e:
                print(f"⚠️ Error al interpretar la función: {e}\nEjemplo válido: x**2 + y - z")

    def preguntar_restricciones(self):
        respuesta = input("¿La función tiene restricciones? (si/no): ").strip().lower()
        if respuesta in ("si", "s", "sí"):
            # mapear nombres a los mismos Symbol de la expresión para evitar símbolos distintos
            locals_map = {s.name: s for s in self.variables}
            print(f"Variables detectadas: {[s.name for s in self.variables]}")
            while True:
                restr = input("Ingrese una restricción (ejemplo: x > 0), o 'fin' para terminar: ").strip()
                if restr.lower() == "fin":
                    break
                if not restr:
                    print("No ingresaste nada. Intenta de nuevo o escribe 'fin' para terminar.")
                    continue
                try:
                    r = sp.sympify(restr, locals=locals_map)
                    # comprobar que la restricción usa sólo variables de la función (por nombre)
                    restr_vars = {s.name for s in r.free_symbols}
                    expr_vars = {s.name for s in self.variables}
                    desconocidas = restr_vars - expr_vars
                    if desconocidas:
                        print(f"⚠️ La restricción usa variables desconocidas: {sorted(list(desconocidas))}. "
                              f"Usa sólo: {sorted(list(expr_vars))}")
                        continue
                    self.restricciones.append(r)
                except Exception as e:
                    print(f"⚠️ Restricción inválida: {e}")

    def mostrar_informacion(self):
        print("\n📌 Información de la función:")
        print(f"Función ingresada: {self.expresion}")
        if self.variables:
            print("Variables identificadas:", [s.name for s in self.variables])
        else:
            print("Variables identificadas: Ninguna (constante)")
        if self.restricciones:
            print("Restricciones:")
            for r in self.restricciones:
                print(" -", r)
        else:
            print("Sin restricciones.")

def main():
    f = Funcion()
    f.ingresar_funcion()
    f.preguntar_restricciones()
    f.mostrar_informacion()

if __name__ == "__main__":
    main()

