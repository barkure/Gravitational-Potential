# Function: 计算地球不同纬度处的重力加速度
import math

# 定义常量
G = 6.672e-11  # 万有引力常量
M = 5.976e24  # 地球质量
R = 6.371e6  # 地球半径
T = 24 * 3600  # 地球自转周期
pi = math.pi  # 圆周率

# 定义纬度
latitudes = [0, 15, 30, 45, 60, 75, 90]

# 计算重力加速度
for latitude in latitudes:
    # 计算纬度角
    phi = latitude * pi / 180
    # 计算角频率
    omega = 2 * pi / T
    # 计算重力加速度
    term1 = G * M / (R ** 2) * math.sin(phi)
    term2 = G * M / (R ** 2) * math.cos(phi) - omega ** 2 * R * math.cos(phi)
    g = math.sqrt(term1 ** 2 + term2 ** 2)
    # 输出结果
    print("纬度为%d度时，重力加速度为%.10f m/s^2" % (latitude, g))