from sympy import symbols, diff, sqrt

# 定义符号，使用大写字母方便后续计算
X, Y, Z, r, R, G, M, pi, sigma, H = symbols('X Y Z r R G M pi sigma H')

# 计算 r
r = sqrt(X**2 + Y**2 + (Z-H)**2)

# 定义 V
# 引力场中任意P点的位等于将一单位质量从无穷远处移至P点时场力所做的功
# r < R
V1 = G*M/R - 2*G*pi*sigma*(r**2 - R**2)/3
# r > R
V2 = G*M/r

# 计算 V 关于 x 的导数
Vx1 = diff(V1, X)
Vx2 = diff(V2, X)

print(Vx1)
print(Vx2)
