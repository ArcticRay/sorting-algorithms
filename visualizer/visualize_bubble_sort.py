import matplotlib.pyplot as plt

languages = ["Python", "C++", "Java"]
times = [0.245, 0.036, 0.050]  # Beispiel-Laufzeiten

plt.bar(languages, times, color=["blue", "green", "orange"])
plt.xlabel("Programming Languages")
plt.ylabel("Time (seconds)")
plt.title("Bubble Sort Performance")
plt.show()
