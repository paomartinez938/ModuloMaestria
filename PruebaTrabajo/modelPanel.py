import numpy as np
import pandas as pd
from scipy.optimize import fsolve

def evaluate_model(G, T):
	# parameters
	R_sh = 545.82  # Resistencia en paralelo
	k_i = 0.037  # Coeficiente de temperatura
	T_n = 298  # Temperatura de referencia
	q = 1.60217646e-19  # Carga del electrón
	n = 1.0  # Factor de idealidad
	K = 1.3806503e-23  # Constante de Boltzmann
	E_g0 = 1.1  # Energía de banda prohibida
	R_s = 0.39  # Resistencia en serie
	num_panels_series = 4  # Número de paneles en serie
	num_panels_parallel = 3  # Número de paneles en paralelo
	I_sc = 9.35 * num_panels_parallel  # Corriente de cortocircuito
	V_oc = 47.4 * num_panels_series  # Voltaje de circuito abierto
	N_s = 72 * num_panels_series  # Número de células en serie
	# evaluate
	I_rs = I_sc / (np.exp((q * V_oc) / (n * N_s * K * T)) - 1)
	# Cálculo de I_o: corriente de saturación inversa
	I_o = I_rs * (T / T_n) * np.exp((q * E_g0 * (1 / T_n - 1 / T)) / (n * K))
	# Cálculo de I_ph: corriente fotogenerada
	I_ph = (I_sc + k_i * (T - 298)) * (G / 1000)
	# Creación de un vector de voltaje desde 0 hasta V_oc con 1000 puntos
	Vpv = np.linspace(0, V_oc, 100)
	# Inicialización de vectores de corriente y potencia
	Ipv = np.zeros_like(Vpv)
	Ppv = np.zeros_like(Vpv)
	# Función para la ecuación del modelo PV
	def f(I, V):
		return (I_ph - I_o * (np.exp((q * (V + I * R_s)) / (n * K * N_s * T)) - 1) - (V + I * R_s) / R_sh - I)
	# Cálculo de la corriente para todo el array de voltaje usando fsolve y vectorización
	Ipv = fsolve(f, I_sc * np.ones_like(Vpv), args=(Vpv))
	Ppv = Vpv * Ipv  # Cálculo vectorizado de la potencia
	# Creación de un DataFrame con resultados
	resultados = pd.DataFrame({'Corriente (A)': Ipv, 'Voltaje (V)': Vpv, 'Potencia (W)': Ppv})
	# Encontrar el punto de máxima potencia
	max_power_idx = resultados['Potencia (W)'].idxmax()
	Vmpp = resultados.loc[max_power_idx, 'Voltaje (V)']
	Impp = resultados.loc[max_power_idx, 'Corriente (A)']
	P_max = resultados.loc[max_power_idx, 'Potencia (W)']
	return resultados, Vmpp, Impp, P_max