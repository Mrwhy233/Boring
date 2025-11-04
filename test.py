import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# --- 基本设置 ---
fig, ax = plt.subplots(figsize=(6, 9))
ax.set_xlim(-2, 2)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')

# 地面
ax.plot([-2, 2], [1, 1], color='dimgray', lw=2)

# --- 构建人体结构比例 ---
head_center = (0, 7.8)
head_radius = 0.35
body_top = 7.45
body_bottom = 3.2

# 头部
head = Circle(head_center, head_radius, fill=False, color='black', lw=2)
ax.add_patch(head)

# 身体主干
ax.plot([0, 0], [body_top, body_bottom], color='black', lw=2)

# 左臂（自然下垂）
ax.plot([0, -0.6], [7.2, 5.8], color='black', lw=2)

# 右臂（伸起拿烟）
right_arm_x = [0, 0.5, 0.8]
right_arm_y = [7.0, 6.8, 6.5]
ax.plot(right_arm_x, right_arm_y, color='black', lw=2)

# 香烟（小橙色线）
ax.plot([0.8, 0.9], [6.5, 6.5], color='orange', lw=3)

# 双腿
ax.plot([0, -0.4], [3.2, 1], color='black', lw=2)   # 左腿
ax.plot([0, 0.4], [3.2, 1], color='black', lw=2)    # 右腿

# 脚
ax.plot([-0.5, -0.3], [1, 1], color='black', lw=2)
ax.plot([0.3, 0.5], [1, 1], color='black', lw=2)

# --- 烟雾动画 ---
num_points = 300
t = np.linspace(0, 12, num_points)
r = 0.05 * t
omega = 4

# 烟从香烟出发（初始点 0.9, 6.5）
smoke_x = np.cos(omega * t) * r + 0.9
smoke_y = 6.5 + 0.12 * t

smoke_line, = ax.plot([], [], color='gray', lw=1.5, alpha=0.6)

def update(frame):
    # 烟雾缓缓上升的部分
    n = frame % num_points
    smoke_line.set_data(smoke_x[:n], smoke_y[:n])
    # 让上层烟雾逐渐变淡
    alpha_fade = np.clip(1 - frame/num_points, 0.2, 0.6)
    smoke_line.set_alpha(alpha_fade)
    return smoke_line,

ani = FuncAnimation(fig, update, frames=num_points, interval=60, blit=True)

plt.show()