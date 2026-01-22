plt.hist(df2,
         bins=20,
         alpha=0.7,
         color=['red','yellow'],
         label='GDP')
plt.title("National GDPs")
plt.xlabel("GDP in Dollars")
plt.ylabel("Frequency")
plt.show()

iris.boxplot(column=["sepal_length", "petal_length"],by="species")
plt.show()

sns.boxplot(x="sex", y="total_bill", hue="day", data=tips)

plt.scatter(df1['Population'],df1['GDP_per_Capita'],
            marker='*',  color='red',
            alpha=0.7,    s = 124)

from pandas.plotting import scatter_matrix
scatter_matrix(df3)
plt.show()

d1.set_index('country').plot.bar(rot=0, title='Rankings', figsize=(15,10), fontsize=12)

df3.plot(kind='bar', stacked=True)

sns.barplot(x="sex", y="survived", hue="alone", data=titanic);


plt.pie(
    d1['InfluenceAggregate'],    labels=d1['country'])

plt.plot(df3['Happiness Score']) #line


  df.stack() #STACK() - Pivot columns into rows

   df.unstack() #UNSTACK() - Pivot index into columns

  pd.melt(df, id_vars=None, value_vars=None) # - Unpivot wide to long

 pd.crosstab(index, columns, values=None, aggfunc=None,
               margins=False, normalize=False)
pd.pivot_table(df, values=None, index=None, columns=None,
                  aggfunc='mean', fill_value=None, margins=False)

pd.concat([df1, df2])

y = pd.merge(gdp,gfp[['Country', 'Manpower Available', 'Railway Coverage (km)']],
                 on='Country',how='left')

set2.intersection(set1)

if (len(a)>=10 & len(a[:7]))>10:
#      print('hello world')
# elif a.count('a')>=25 or b.count('a')<=10:
#      print('hello mars')
# else:
#      print('Aynur is intelligent')

arr3=[[1,45,76,25],[41,22,12,21],[21,32,45,12]]
narr3=np.array(arr3)
narr4=np.zeros((4,2))

np.concatenate([narr1,b])

print(narr10+narr1)
print(np.add(narr10,narr1))
print(narr1-narr10)
print(np.subtract(narr1,narr10))
print(narr1/narr10)
print(np.divide(narr10,narr1))
print(narr1*narr10) #hadmard product
print(np.dot(narr10,narr1)) #dot product
print(np.absolute([-25,12]))
print(np.amin(narr3))
print(np.min(narr3))
print(np.amax(narr3))
print(np.max(narr3))
print(np.add(3,narr10))
print(np.all(narr5))
print(np.multiply(narr5, narr1))
print(np.exp(narr10))
unsorted=np.random.randn(10)
s1=np.array(['desk','chair','bulb'])
s2=np.array(['lamp','bulb','chair'])

print(np.intersect1d(s1,s2))
print(np.union1d(s1,s2))
print(np.setdiff1d(s1,s2))
print(np.setdiff1d(s2,s1))
print(np.in1d(s1,s2))
print(np.setxor1d(s1,s2))
val2=np.random.randint(5, size=(5,2)) #Return random integers from low (inclusive) to high (exclusive)
val3=np.random.random_sample(10) #Return random floats in the half-open interval [0.0, 1.0).
val4=np.random.random_integers(5, 10, size=(5)) #Random integers of type np.int between low and high, inclusive
print(val4)
data1 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))