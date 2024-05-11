import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义 sigma, G, R, H
sigma = 1*1000 # rho: g/cm^3 to kg/m^3
G = 6.67e-11
R = 50
H = 100

# 计算 M
M = 4/3*np.pi*R**3*sigma

# 定义网格
X, Y = np.meshgrid(np.arange(-500, 501, 10), np.arange(-500, 501, 10))
Z = 0

# 计算 Vz
Vz = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                -2*G*np.pi*sigma*(-2*H + 2*Z)/3,
                G*M*(H - Z)/(X**2 + Y**2 + (-H + Z)**2)**(3/2))

# 转换单位
# m/s^2 to g.u.
Vz = Vz * 1e6

# 绘制 Vz
fig = plt.figure()

# 创建第一个子图
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Vz, cmap='viridis', edgecolor='none')
ax1.set_xlabel(r'$X(m)$')
ax1.set_ylabel(r'$Y(m)$')
ax1.set_zlabel(r'$V_z(g.u.)$')
ax1.set_title(r'$V_z\ 3D\ Surface\ Plot$')
fig.colorbar(surf, ax=ax1, orientation='horizontal')

# 创建第二个子图
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Vz, cmap='viridis')
ax2.axis('equal')
ax2.set_xlabel(r'$X(m)$')
ax2.set_ylabel(r'$Y(m)$')
ax2.set_title(r'$V_z\ Contour\ Plot$')
cbar = fig.colorbar(mappable=contour, ax=ax2, orientation='horizontal')
cbar.set_label(r'$g.u.$')

plt.show()

