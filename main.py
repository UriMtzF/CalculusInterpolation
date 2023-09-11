import numpy as np
from scipy.interpolate import CloughTocher2DInterpolator

# Definir la lista de puntos como un arreglo NumPy
points = np.array([(-2,-3,0.2), (-2,-2,0.3), (-2,-1,0.2), (-2,0,0.2), (-2,1,0), (-2,2,0), (-1,-3,0.2), (-1,-2,0.3), (-1,-1,0.3), (-1,0,0.3), (-1,1,0), (-1,2,0), (0,-3,0.2), (0,-2,0.2), (0,-1,0.3), (0,0,1), (0,1,0.2), (0,2,0), (1,-3,0), (1,-2,0.2), (1,-1,0.2), (1,0,1), (1,1,0.7), (1,2,0.2), (2,-3,0.2), (2,-2,0.2), (2,-1,0.2), (2,0,1.5), (2,1,0), (2,2,0), (3,-3,0.3), (3,-2,0.7), (3,-1,0.3), (3,0,0.5), (3,1,0), (3,2,0), (4,-3,0.2), (4,-2,0.2), (4,-1,0.2), (4,0,0), (4,1,0), (4,2,0)])

# Separar los puntos en las coordenadas x, y y los valores z
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Crear un interpolador por splines cúbicos
interpolator = CloughTocher2DInterpolator(points[:, :2], z)

# Ahora puedes evaluar el interpolador en cualquier punto (x, y)
x_eval = 0.5  # Cambia estos valores según tus necesidades
y_eval = 1  # Cambia estos valores según tus necesidades
result = interpolator(x_eval, y_eval)
print(f'f({x_eval}, {y_eval}) = {result}')
