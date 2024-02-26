import plotly.graph_objects as go
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
print(z)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(scene=dict(xaxis_title='X Axis',yaxis_title='Y Axis',zaxis_title='Z Axis'),
                  margin=dict(l=0, r=0, b=0, t=40),
                  title='3D Surface Plot of sin(sqrt(x^2 + y^2))')
fig.show()