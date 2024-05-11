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
X = np.arange(-200, 201, 5)
Y = 0
Z = 0

# V 及其导数
# 计算 V
V_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2, 
             -2*G*np.pi*sigma*((X**2 + Y**2 + (Z-H)**2) - R**2)/3 + G*M/R, 
             G*M/np.sqrt(X**2 + Y**2 + (Z-H)**2))

# 计算 Vx_slice
Vx_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                -4*G*np.pi*sigma*X/3,
                -G*M*X/(X**2 + Y**2 + (Z-H)**2)**1.5)

# 计算 Vx_slice
Vy_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                -4*G*np.pi*sigma*Y/3,
                -G*M*Y/(X**2 + Y**2 + (Z-H)**2)**1.5)

# 计算 Vz_slice
Vz_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                -2*G*np.pi*sigma*(-2*H + 2*Z)/3,
                G*M*(H - Z)/(X**2 + Y**2 + (-H + Z)**2)**(3/2))

# 转换单位
# 1e-6 m^2/s^2
V_slice = V_slice * 1e6
# m/s^2 to g.u.
Vx_slice = Vx_slice * 1e6
Vy_slice = Vy_slice * 1e6
Vz_slice = Vz_slice * 1e6

# 绘制剖面图
fig = plt.figure()

# 绘制 V_slice
# 创建第一个子图
ax1 = fig.add_subplot(121)
ax1.plot(X, V_slice)
ax1.set_xlabel(r'$X(m)$')
ax1.set_ylabel(r'$V(10^{-6} m^2/s^2)$')
ax1.set_title(r'$V\ Slice$')

# 绘制 V_diff_slice
# 创建第二个子图
ax2 = fig.add_subplot(122)
ax2.plot(X, Vx_slice, label='Vx')
ax2.plot(X, Vy_slice, label='Vy')
ax2.plot(X, Vz_slice, label='Vz')
ax2.set_xlabel(r'$X(m)$')
ax2.set_ylabel(r'$V_{diff}(g.u.)$')
ax2.set_title(r'$V_{diff}\ Slice$')
ax2.legend()

plt.show()


# 二阶导数
# 计算 Vxx_slice
Vxx_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                -4*G*np.pi*sigma/3,
                3*G*M*X**2/(X**2 + Y**2 + (-H + Z)**2)**(5/2) - G*M/(X**2 + Y**2 + (-H + Z)**2)**(3/2))

# 计算 Vyy_slice
Vyy_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                -4*G*np.pi*sigma/3,
                3*G*M*Y**2/(X**2 + Y**2 + (-H + Z)**2)**(5/2) - G*M/(X**2 + Y**2 + (-H + Z)**2)**(3/2))

# 计算 Vzz_slice
Vzz_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                -4*G*np.pi*sigma/3,
                G*M*(H - Z)*(3*H - 3*Z)/(X**2 + Y**2 + (-H + Z)**2)**(5/2) - G*M/(X**2 + Y**2 + (-H + Z)**2)**(3/2))

# 计算 Vxy_slice
Vxy_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                0,
                3*G*M*X*Y/(X**2 + Y**2 + (-H + Z)**2)**(5/2))

# 计算 Vxz_slice
Vxz_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                0,
                -G*M*X*(3*H - 3*Z)/(X**2 + Y**2 + (-H + Z)**2)**(5/2))

# 计算 Vyz_slice
Vyz_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                0,
                -G*M*Y*(3*H - 3*Z)/(X**2 + Y**2 + (-H + Z)**2)**(5/2))

# 转换单位
# 1/s^2 to E
Vxx_slice = Vxx_slice * 1e9
Vyy_slice = Vyy_slice * 1e9
Vzz_slice = Vzz_slice * 1e9
Vxy_slice = Vxy_slice * 1e9
Vxz_slice = Vxz_slice * 1e9
Vyz_slice = Vyz_slice * 1e9

# 绘制剖面图
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(X, Vxx_slice, label='Vxx')
ax1.plot(X, Vyy_slice, label='Vyy')
ax1.plot(X, Vzz_slice, label='Vzz')
ax1.plot(X, Vxy_slice, label='Vxy')
ax1.plot(X, Vxz_slice, label='Vxz')
ax1.plot(X, Vyz_slice, label='Vyz')
ax1.set_xlabel(r'$X(m)$')
ax1.set_ylabel(r'$V_{diff2}(E)$')                                   
ax1.set_title(r'$V_{diff2}\ Slice$')
ax1.legend()

plt.show()


# 三阶导数
# 计算 Vzzz_slice
Vzzz_slice = np.where(X**2 + Y**2 + (Z-H)**2 < R**2,
                0,
                G*M*(H - Z)*(3*H - 3*Z)*(5*H - 5*Z)/(X**2 + Y**2 + (-H + Z)**2)**(7/2) - 3*G*M*(H - Z)/(X**2 + Y**2 + (-H + Z)**2)**(5/2) - 2*G*M*(3*H - 3*Z)/(X**2 + Y**2 + (-H + Z)**2)**(5/2))

# 转换单位
# 1/(m*s^2) to nMKS
Vzzz_slice = Vzzz_slice * 1e9

# 绘制剖面图
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(X, Vzzz_slice, label='Vzzz')
ax1.set_xlabel(r'$X(m)$')
ax1.set_ylabel(r'$V_{zzz}(nMKS)$')
ax1.set_title(r'$V_{zzz}\ Slice$')
ax1.legend()

plt.show()