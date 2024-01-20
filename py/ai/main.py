import numpy as np
import matplotlib.pyplot as plt

#Входные и выходные веса
weighst_input_to_hidden = np.random.uniform(-0.5,0.5, (4, 5))
weighst_hidden_to_output = np.random.uniform(-0.5,0.5, (3, 4))

# Нейрон смешения
bias_input_to_hidden = np.zeros((4,1))
bias__hidden_to_output = np.zeros((3,1))