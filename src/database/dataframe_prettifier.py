import pandas as pd
from functools import wraps

def prettify_output(func):
    """
    Decorador que imprime el DataFrame con un marco visual ajustado dinámicamente al contenido.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, pd.DataFrame):
            df_str = result.to_string(index=False)
            lines = df_str.splitlines()
            max_width = max(len(line) for line in lines) if lines else 30

            header = f"| {'RESULTADOS'.center(max_width)} |"
            border = "+" + "-" * (max_width + 2) + "+"

            print("\n" + border)
            print(header)
            print(border)

            if result.empty:
                print(f"| {'(DataFrame vacío)'.center(max_width)} |")
            else:
                for line in lines:
                    print(f"| {line.ljust(max_width)} |")

            print(border + "\n")
        else:
            print(f"\n[Advertencia] Resultado no es un DataFrame: {type(result)}\n")

        return result

    return wrapper
