import load_data
import matplotlib.pyplot as plt

#sort
data = load_data.load_data('data/activity.csv')
power_W = data['PowerOriginal']
print(power_W)
sorted_power_W_neu = load_data.bubble_sort(power_W)
print(sorted_power_W_neu[::-1])


# Plotting the sorted data
plt.plot(sorted_power_W_neu[::-1])
plt.title('Sorted Power Data')
plt.xlabel('Zeit [s]')
plt.ylabel('Power (W)')
plt.savefig('figures/sorted_power_data.png')
plt.show()
