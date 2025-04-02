import pandas as pd
import  numpy as np

num_registros = 8000
np.random.seed(42)
data = {
    "id_persona": np.arange(1, num_registros + 1),
    "genero": np.random.choice(['m', 'f', 'otro'], num_registros),
    "edad": np.random.randint(18, 63, num_registros),
    "nacionalidad": np.random.randint(1, 3, num_registros),
    "categoria_municipio": np.random.randint(1, 7, num_registros),
    "ingresos": np.random.randint(1423000, 22000000, num_registros),
    "actividad": np.random.choice(['Ama de casa', 'Estudiante', 'Empleado','Independiente', 'Otro'], num_registros),

}
df = pd.DataFrame(data)

df.to_csv('datos_socioecomicos.csv', index=False)


