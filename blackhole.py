import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ==========================================
#     黑洞引力模拟器 v1.0
# ==========================================

G = 6.674e-11          # 万有引力常数
M = 5e30               # 黑洞质量（约为太阳质量的25倍）
c = 3e8                # 光速
dt = 0.1               # 时间步长

# ------------------------------------------
# 模式1：牛顿引力轨迹（静态）
# ------------------------------------------
def newtonian_static():
    r = np.array([1e10, 0.0])
    v = np.array([0.0, 5e4])
    steps = 5000
    positions = []

    for _ in range(steps):
        r_mag = np.linalg.norm(r)
        a = -G * M * r / r_mag**3
        v += a * dt
        r += v * dt
        positions.append(r.copy())

    positions = np.array(positions)

    plt.figure(figsize=(6,6))
    plt.plot(positions[:,0], positions[:,1], color='cyan')
    plt.scatter(0, 0, color='black', s=200, label='Black Hole')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Newtonian Gravity - Particle Trajectory')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# ------------------------------------------
# 模式2：牛顿引力动画
# ------------------------------------------
def newtonian_animation():
    r = np.array([1e10, 0.0])
    v = np.array([0.0, 6e4])
    steps = 2000
    dt_anim = 0.05
    positions = []

    for _ in range(steps):
        r_mag = np.linalg.norm(r)
        a = -G * M * r / r_mag**3
        v += a * dt_anim
        r += v * dt_anim
        positions.append(r.copy())

    positions = np.array(positions)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-1.2e10, 1.2e10)
    ax.set_ylim(-1.2e10, 1.2e10)
    ax.set_aspect('equal')
    ax.set_facecolor("black")

    blackhole = plt.Circle((0,0), 2e9, color='gray')
    ax.add_artist(blackhole)
    particle, = ax.plot([], [], 'o', color='cyan')

    def update(i):
        particle.set_data(positions[i,0], positions[i,1])
        return particle,

    ani = animation.FuncAnimation(fig, update, frames=len(positions), interval=20, repeat=False)
    plt.title("Particle Falling into a Black Hole (Animation)")
    plt.show()


# ------------------------------------------
# 模式3：广义相对论近似轨迹
# ------------------------------------------
def relativistic_orbit():
    dt_rel = 0.01
    steps = 10000
    r = 1e10
    v_r = 0
    v_t = 4e7
    L = r * v_t
    positions = []

    for i in range(steps):
        a_r = -G*M/r**2 + L**2/r**3 - 3*G*M*L**2/(c**2 * r**4)
        v_r += a_r * dt_rel
        r += v_r * dt_rel
        theta = L * dt_rel / r**2
        positions.append([
            r * np.cos(theta*i),
            r * np.sin(theta*i)
        ])

    positions = np.array(positions)

    plt.figure(figsize=(6,6))
    plt.plot(positions[:,0], positions[:,1], color='orange')
    plt.scatter(0, 0, color='black', s=200, label='Black Hole')
    plt.title("Relativistic Orbit Near a Black Hole")
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()


# ------------------------------------------
# 主菜单
# ------------------------------------------
def main():
    print("""
=============================================
         🌀 黑洞引力模拟器 v1.0
=============================================
请选择模拟模式：

1️⃣ 牛顿引力（静态轨迹）
2️⃣ 牛顿引力（动态动画）
3️⃣ 广义相对论近似轨迹
0️⃣ 退出
=============================================
    """)

    while True:
        mode = input("请输入模式编号：").strip()
        if mode == '1':
            newtonian_static()
        elif mode == '2':
            newtonian_animation()
        elif mode == '3':
            relativistic_orbit()
        elif mode == '0':
            print("已退出。")
            break
        else:
            print("无效输入，请重新选择。")

# 运行主程序
if __name__ == "__main__":
    main()