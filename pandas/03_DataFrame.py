# DataFrame
# Es como una tabla, varias columnas y filas (similar a Excel).
# Ejemplo:

import pandas as pd
import numpy as np

data = {
    "nombres": ["Ana", "Luis", "Carlos"],
    "Edad": [23, 30, 28],
    "salarios": [2000, 3000, 2500]
}

df = pd.DataFrame(data)
print(df, "\n")
print(df.dtypes, "\n")
# Observe que el tipo d inferido es int64.
# Para imponer un unico tipo d:

df2 = pd.DataFrame({
    "nombres": ["Ana", "Luis", "Carlos"],
    "Edad": pd.Series([23, 30, 28], dtype=np.int8),
    "salarios": pd.Series([2000, 3000, 2500], dtype=np.int32)
})

print(df2.dtypes)
