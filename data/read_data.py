import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import os


# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.realpath(__file__))
# Construct the file path to the CSV file relative to the script directory
filename = os.path.join(script_dir, '..', 'data', 'Real Students Grades.csv')

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    # Skip the header row if needed
    next(csv_reader, None)
    # Iterate over each row in the CSV file
    sat = []
    bagrut = []
    for row in csv_reader:
        if row[0] and row[1] and float(row[1]) > 0:
            sat.append(float(row[0]))
            bagrut.append(float(row[1]))
sat = np.array(sat)
bagrut = np.array(bagrut)

# Visualize the initial data distribution


def show_real_students_distribution():
    plt.figure(figsize=(10, 10))
    plt.xlim(200, 800)
    plt.ylim(0, 120)
    plt.scatter(sat, bagrut, color='blue', s=3)
    plt.xlabel('SAT scores')
    plt.ylabel('Bagrut scores')
    plt.title('Real Students Scores Scatter Plot')
    plt.grid(True)
    plt.savefig("../plots/png/real_students.png")
    plt.savefig("../plots/pdf/real_students.pdf")
    plt.show()

print("number of students: " +str(np.shape(sat))) # number os students

def get_Students():
    students = np.stack((sat, bagrut), axis=1)
    students = pd.DataFrame(students)
    return students

# random points square

def random_square():
    x = []
    y = []
    for i in range(len(sat)):
        x.append(random.random())
        y.append(random.random())
    df = pd.DataFrame({'x': x, 'y': y})
    return df

random_square_df = random_square()

def show_random_square_distribution():
    plt.figure(figsize=(8, 8))
    plt.scatter(random_square_df['x'], random_square_df['y'], color='blue', s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Random Points - Square')
    plt.grid(True)
    plt.savefig("../plots/png/random_square.png")
    plt.savefig("../plots/pdf/random_square.pdf")
    plt.show()

def get_square_df():
    return random_square_df


# random points rhombus

def random_rhombus():
    points = []
    while len(points) < len(sat):
        x = random.random()
        y = random.random()

        # Check if the point falls within the rhombus
        if (x >= 0 and x <= 0.5 and y >= 0.5 - x and y <= 0.5 + x) or \
                (x >= 0.5 and x <= 1 and y >= x - 0.5 and y <= 1.5 - x):
            points.append((x, y))

    # Create a DataFrame from the list of points
    df = pd.DataFrame(points, columns=['x', 'y'])
    return df

random_rhombus_df = random_rhombus()

def show_random_rhombus_distribution():
    plt.figure(figsize=(8, 8))
    plt.scatter(random_rhombus_df['x'], random_rhombus_df['y'], color='blue', s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Random Points - Rhombus')
    plt.grid(True)
    plt.savefig("../plots/png/random_rhombus.png")
    plt.savefig("../plots/pdf/random_rhombus.pdf")
    plt.show()

def get_rhombus_df():
    return random_rhombus()

def random_circle():
    points = []
    radius = 0.5

    while len(points) < len(sat):
        # Generate random x and y coordinates within the square
        x = random.random()
        y = random.random()

        # Calculate the distance from the point to the center of the square
        distance = np.sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2)

        # Check if the point falls within the inscribed circle
        if distance <= radius:
            points.append((x, y))

    # Create a DataFrame from the list of points
    df = pd.DataFrame(points, columns=['x', 'y'])
    return df

random_circle_df = random_circle()

def show_random_circle_distribution():
    # Plot the DataFrame
    plt.figure(figsize=(8, 8))
    plt.scatter(random_circle_df['x'], random_circle_df['y'], color='blue', s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Random Points - in Circle')
    plt.grid(True)
    plt.savefig("../plots/png/random_circle.png")
    plt.savefig("../plots/pdf/random_circle.pdf")
    plt.show()

def get_circle_df():
    return random_circle()