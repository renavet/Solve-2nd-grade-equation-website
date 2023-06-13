import matplotlib.pyplot as plt
import math
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def solve_2g_equ():
    if request.method == 'POST':
        a = int(request.form['a='])
        b = int(request.form['b='])
        c = int(request.form['c='])
        D = (b ** 2) - 4 * a * c
        x_v = -b / (2 * a)
        y_v_f = -(D / (4 * a))
        x_f = -b / (2 * a)

        v = np.array([x_v, y_v_f])
        f = np.array([x_f, y_v_f])
        directrix = -(1 + D) / (4 * a)

        if D >= 0:
            x1 = (-b + np.sqrt(D)) / (2 * a)
            x2 = (-b - np.sqrt(D)) / (2 * a)
            results =(f"la direttrice è x={directrix},il fuoco è {f},il vertice è {v} x1={x1}, x2={x2}")
        else:
            results = "delta minore di zero"

        plt.title('Graph of Quadratic Equation')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        x = np.linspace(-10, 10, 100)
        y = a * (x ** 2) + b * x + c
        plt.plot(x, y, color='lightblue')
        plt.plot(x_v, y_v_f, 'ro', label='Vertex')
        plt.plot(x_f, y_v_f, 'bo', label='Focus')
        plt.legend()
        plt.grid(True)
        plt.savefig('static/plot.png')  # Save the plot image to a file
        plt.close()  # Close the plot to release resources

        return render_template('main.html', results=results)

    return render_template('main.html')

if __name__ == '__main__':
    app.run()

