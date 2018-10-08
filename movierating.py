#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:54:25 2018

@author: deepak
"""
import pandas as pd
pd.options.display.max_columns=100
previous=pd.read_csv('/home/deepak/Downloads/datset/fandango_score_comparison.csv')
after=pd.read_csv('/home/deepak/Downloads/datset/movie_ratings_16_17.csv')
"""print(previous.head(3))
print("DIFFERENCE")
print(after.head(3))
fandango_previous = previous[['FILM', 'Fandango_Stars', 'Fandango_Ratingvalue', 'Fandango_votes',
                             'Fandango_Difference']].copy()
fandango_after = after[['movie', 'year', 'fandango']].copy()

print(fandango_previous.head(10)) 
#print(fandango_after.head(3))
#print(fandango_after.sample(10,random_state=1))
sum=(fandango_previous['Fandango_votes']<30) """
fandango_FILM=previous[['FILM']]
film=fandango_FILM.head(2)
print(film)
print(type(film))
film_15=str(film)
print(type(film_15))
print(film_15)
#length=len(film_15)
#print(length)
#print(film_15[-5:-1])
fandango_previous['Year'] = fandango_previous['FILM'].str[-5:-1]
print(fandango_previous['Year'])
previous_2016=fandango_previous['Year'].value_counts()
print(previous_2016)
fandango_after_film=after[['year']]
after_film=fandango_after_film.head(2)
print(after_film)
print(type(after_film))
film_16=str(after_film)
print(film_16)
print(type(film_16))
fandango_after['year']=fandango_after['year']
print(fandango_after['year'])
after_2015=fandango_after['year'].value_counts()
print(after_2015)
import matplotlib.pyplot as plt
from numpy import arange
#%matplotlib inline
plt.style.use('fivethirtyeight')

previous_2016['Fandango_previous'].plot.kde(label = '2015', legend = True, figsize = (8,5.5))
after_2015['fandango'].plot.kde(label = '2016', legend = True)

plt.title("Comparing distribution shapes for Fandango's ratings\n(2015 vs 2016)",
          y = 1.07) # the `y` parameter pads the title upward
plt.xlabel('Stars')
plt.xlim(0,5) # because ratings start at 0 and end at 5
plt.xticks(arange(0,5.1,.5))
plt.show()

