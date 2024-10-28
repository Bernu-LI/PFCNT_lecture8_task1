import numpy as np
import matplotlib.pyplot as plt

# Ввод данных
m = float(input("Введите массу груза (кг): "))
k = float(input("Введите коэффициент жесткости пружины (Н/м): "))
b = float(input("Введите коэффициент сопротивления среды (Н·с/м): "))

# Начальные условия
x0 = 1.0  # начальное смещение (м)
v0 = 0.0  # начальная скорость (м/с)

# Временные параметры
t_max = 20  # максимальное время (с)
dt = 0.01  # шаг времени (с)
t = np.arange(0, t_max, dt)  # временная сетка


# Функция для вычисления положений и скоростей
def oscillate(m, k, b, x0, v0, t):
    # Принцип решения дифференциального уравнения
    omega0 = np.sqrt(k / m)
    gamma = b / (2 * m)
    omega_d = np.sqrt(omega0 ** 2 - gamma ** 2)

    A = x0
    B = (v0 + gamma * x0) / omega_d

    # Дампированные гармонические колебания
    x = np.exp(-gamma * t) * (A * np.cos(omega_d * t) + B * np.sin(omega_d * t))
    v = np.gradient(x, dt)

    return x, v


# Вычисление положений и скоростей
x, v = oscillate(m, k, b, x0, v0, t)

# Энергии
kinetic_energy = 0.5 * m * v ** 2
potential_energy = 0.5 * k * x ** 2
total_energy = kinetic_energy + potential_energy

# Построение графиков
plt.figure(figsize=(12, 8))

plt.plot(t, kinetic_energy, label='Кинетическая энергия', color='b', linestyle='-')
plt.plot(t, potential_energy, label='Потенциальная энергия', color='g', linestyle='-')
plt.plot(t, total_energy, label='Полная механическая энергия', color='r', linestyle='-')

plt.title('Энергетические превращения при колебании груза на пружине')
plt.xlabel('Время (с)')
plt.ylabel('Энергия (Дж)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()