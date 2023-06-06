import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

height = 100  
g = 9.8  
mass = 1  

def visualize_custom_graph(mass, g, height, color, curve):
    def linear_curve(mass, t):
        return height - (mass * g) * t
    def parabolic_curve(mass, t):
        end_point_x = np.sqrt(2 * height / (mass * g))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)
    def circular_curve(mass,t):
        end_point_x = 2 * np.sqrt(height / (mass * g))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)
    def cycloid_curve(mass_d,t):
        end_point_x = (2 * height / np.pi) * np.sqrt(np.pi / (2 * (mass_d * g) * height))
        slope = -height / end_point_x
        a = -height / (end_point_x**2)
        return 2 * (slope * t + height) - (a * t**2 + height)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(curve)
    if color == 'red':
        color = 'r'
    elif color == 'green':
        color = 'g'
    elif color == 'blue':
        color = 'b'    
    if curve == 'linear curve':
        linear_time_to_reach_zero = height / (mass * g)
        ax.set_xlim(0, linear_time_to_reach_zero)
        ax.set_ylim(0, height)
        linear_line, = ax.plot([], [], f'{color}-', label='Linear')
        linear_point, = ax.plot([], [], f'{color}o', label=f'Linear: {linear_time_to_reach_zero:.2f}s')
        def update(frame):
            t = np.linspace(0, frame, 100)
            linear_line.set_data(t, linear_curve(mass, t))
            linear_point.set_data([linear_time_to_reach_zero], [linear_curve(mass, linear_time_to_reach_zero)])

            return linear_line, linear_point
        animation = FuncAnimation(
            fig,
            update,
            frames=np.arange(0, linear_time_to_reach_zero, 0.1),
            blit=True
        )
        fig.tight_layout()
        ax.set_xlabel('Time')
        ax.set_ylabel('Height')
        ax.legend()
        plt.show()
    elif curve == 'parabolic curve':
        parabolic_time_to_reach_zero = np.sqrt(2 * height / (mass * g))
        ax.set_xlim(0, parabolic_time_to_reach_zero)
        ax.set_ylim(0, height)
        parabolic_line, = ax.plot([], [], f'{color}-', label='Parabolic')
        parabolic_point, = ax.plot([], [], f'{color}o', label=f'Parabolic: {parabolic_time_to_reach_zero:.2f}s')
        def update(frame):
            t = np.linspace(0, frame, 100)
            parabolic_line.set_data(t, parabolic_curve(mass, t))
            parabolic_point.set_data([parabolic_time_to_reach_zero], [parabolic_curve(mass, parabolic_time_to_reach_zero)])
            return parabolic_line, parabolic_point
        animation = FuncAnimation(
            fig,
            update,
            frames=np.arange(0, parabolic_time_to_reach_zero, 0.1),
            blit=True
        )
        fig.tight_layout()
        ax.set_xlabel('Time')
        ax.set_ylabel('Height')
        ax.legend()
        plt.show()
    elif curve == 'circular curve':
        circular_time_to_reach_zero = 2 * np.sqrt(height / (mass * g))
        ax.set_xlim(0, circular_time_to_reach_zero)
        ax.set_ylim(0, height)
        circular_line, = ax.plot([], [], f'{color}-', label='Circular')
        circular_point, = ax.plot([], [], f'{color}o', label=f'Circular: {circular_time_to_reach_zero:.2f}s')
        def update(frame):
            t = np.linspace(0, frame, 100)
            circular_line.set_data(t, circular_curve(mass, t))
            circular_point.set_data([circular_time_to_reach_zero], [circular_curve(mass, circular_time_to_reach_zero)])
            return circular_line, circular_point
        animation = FuncAnimation(
            fig,
            update,
            frames=np.arange(0, circular_time_to_reach_zero, 0.1),
            blit=True
        )
        fig.tight_layout()
        ax.set_xlabel('Time')
        ax.set_ylabel('Height')
        ax.legend()
        plt.show()
        
    elif curve == 'cycloid curve':
        cycloid_time_to_reach_zero = (2 * height / np.pi) * np.sqrt(np.pi / (2 * (mass * g) * height))
        ax.set_xlim(0, cycloid_time_to_reach_zero)
        ax.set_ylim(0, height)
        cycloid_line, = ax.plot([], [], f'{color}-', label='Cycloidal')
        cycloid_point, = ax.plot([], [], f'{color}o', label=f'Cycloidal: {cycloid_time_to_reach_zero:.2f}s')
        def update(frame):
            t = np.linspace(0, frame, 100)

            cycloid_line.set_data(t, cycloid_curve(mass, t))
            cycloid_point.set_data([cycloid_time_to_reach_zero], [cycloid_curve(mass, cycloid_time_to_reach_zero)])

            return cycloid_line, cycloid_point
        animation = FuncAnimation(
            fig,
            update,
            frames=np.arange(0, cycloid_time_to_reach_zero, 0.1),
            blit=True
        )
        fig.tight_layout()
        ax.set_xlabel('Time')
        ax.set_ylabel('Height')
        ax.legend()
        
        plt.show()