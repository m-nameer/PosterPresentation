import matplotlib.pyplot as plt

freelance_earnings = {'IT': 156.9, 'Non-IT': 112.9}
total_earnings = sum(freelance_earnings.values())


it_contribution = (freelance_earnings['IT'] / total_earnings) * 100


plt.figure(figsize=(6, 6))
x = freelance_earnings.keys()
y = freelance_earnings.values()
plt.bar(x, y)


for i, v in enumerate(y):
  plt.text(i, v + 2, f"US$ {v:.1f} million", va='bottom', ha='center', fontsize=10)  # Adjust the label position and format


plt.title('Pakistan Freelancing Earnings (July-March FY2023)')
plt.xlabel('Freelancing Sector')
plt.ylabel('Earnings (in Million USD)')


plt.xticks(rotation=0)
plt.tight_layout()
plt.show()