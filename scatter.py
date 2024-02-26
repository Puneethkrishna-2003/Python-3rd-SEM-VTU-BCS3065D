import matplotlib.pyplot as plt

countries = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
population = [213993437, 145912025, 1393409038, 1444216107, 61608912]
per_capita_income = [9600, 11600, 2300, 11000, 6500]

circlesize=[]
for i in range(len(population)):
    circlesize.append(population[i]/1000000)

print(circlesize)
color=range(len(population))
scatter = plt.scatter(population, per_capita_income,s=circlesize,c=color)

for i, country in enumerate(countries):
    plt.annotate(country, (population[i], per_capita_income[i]),textcoords="offset points",ha="center",xytext=(0,5))

plt.colorbar(scatter, label='Index')

plt.xlabel('Population')
plt.ylabel('Per Capita Income (USD)')
plt.title('Population vs Per Capita Income of BRICS Nations')

plt.show()
