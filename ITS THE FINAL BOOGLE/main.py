from pyscript import document, display
import numpy as np

# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

# Preload to avoid font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data globally
days = []
absences = []


def displaying(e):
    day = document.getElementById('dayOfTheWeek').value
    absence = int(document.getElementById('absences').value)

    # Save data
    days.append(day)
    absences.append(absence)

    # Convert to NumPy array
    converted_absences = np.array(absences)

    # Clear previous plot
    plt.clf()

    # Create graph
    plt.plot(days, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    # Display plot
    plt.show()