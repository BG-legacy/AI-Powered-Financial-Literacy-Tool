import matplotlib.pyplot as plt
import numpy as np

# Data
models = ['GPT-4', 'GPT-3.5', 'FinBERT', 'BERT', 'T5']
accuracy = [92, 85, 90, 80, 75]
speed = [180, 200, 150, 300, 250]

# Plot
x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, accuracy, width, label='Accuracy (%)')
rects2 = ax.bar(x + width/2, speed, width, label='Speed (ms)')

ax.set_xlabel('Models')
ax.set_title('Model Performance Comparison')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

plt.show()