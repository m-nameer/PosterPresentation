import matplotlib.pyplot as plt

fiscal_years = ['FY 2019-20', 'FY 2020-21', 'FY 2021-22', 'FY 2022-23']


exports = [150, 151, 178, 199]


plt.figure(figsize=(8, 6))
plt.bar(fiscal_years, exports, color=['lightblue', 'skyblue', 'deepskyblue', 'dodgerblue'])
plt.xlabel('Fiscal Year')
plt.ylabel('IT & Telecommunication Exports (in Billion USD)')
plt.title('India\'s IT & Telecommunication Exports')
plt.xticks(rotation=360)


plt.tight_layout()
plt.show()