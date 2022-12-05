import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

adv_stats = pd.read_csv('/Users/annamartirosyan/PycharmProjects/NBA_salaries/data/player_data_wrangled/players2022/Adv_2022wrangled.csv')
adv_stats.drop(adv_stats.columns[[0, 1,  3, 4, 5, 18, 23,28,29]], axis = 1, inplace = True)


perGame = pd.read_csv('/Users/annamartirosyan/PycharmProjects/NBA_salaries/data/player_data_wrangled/players2022/PerGame_2022wrangled.csv')
perGame.drop(perGame.columns[[0, 1, 18, 23]], axis=1, inplace=True)

perGameAdv = perGame.merge(adv_stats, on='Player', how='inner')

fa = pd.read_csv('/Users/annamartirosyan/PycharmProjects/NBA_salaries/data/salary_data/fixed_fa_signings/2022.csv')
fa.drop(fa.columns[[0,2,3,4,5,6,7,10]], axis=1, inplace=True)


final = perGameAdv.merge(fa, left_on = 'fix', right_on = 'name', how = 'inner')
# drop 'fix' and 'name'
final.drop(final.columns[[27]], axis = 1, inplace = True)
final.head()
final2 = final.copy(deep=True)
print(final.columns)
final.drop(final.columns[[0, 26,25, 46]], axis = 1, inplace = True)

# Check correlation between features
colormap = plt.cm.magma
sns.set(font_scale=1)
plt.figure(figsize=(30,30))

plt.title('Pearson Correlation of NBA Salary Features', y=1.05, size=50)

#make all values floating points, compute pairwise correlation of columns,
# excluding NA/null values

corr = final.astype(float).corr().round(2)
mask = np.zeros_like(corr, dtype=bool)

# mask upper diagonal of heatmap
mask[np.triu_indices_from(mask)] = True

fig1 = sns.heatmap(corr,
                   mask=mask,
                   linewidths=0.1,
                   vmax=1.0,
                   square=True,
                   cmap=colormap,
                   linecolor='white',
                   annot=True)

fig1.figure.savefig("correlation_table.png")

########################################################################################################################
print(final2.columns)
#Selecting candidates
final2.drop(final2.columns[[0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 21,
                         25, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                         41, 42]], axis = 1, inplace = True)
# print(final2.columns)
#

#
# Index(['MP', 'FG', 'FGA', 'FT', 'DRB', 'STL', 'BLK', 'TOV', 'PS.G', 'PER',
#        'DWS', 'OBPM', 'DBPM', 'BPM', 'VORP', 'total-contract', 'average'],
#       dtype='object')
 #piti mnan sranq



# #Check correlation between features
# sns.set(font_scale=2)
# colormap = plt.cm.magma
# plt.figure(figsize=(30,30))
#
# plt.title('Pearson Correlation of NBA Salary Features', y=1.05, size=50)
#
# corr = final2.astype(float).corr().round(2)
#
# mask = np.zeros_like(corr, dtype=bool)
#
# # mask upper diagonal of heatmap
# mask[np.triu_indices_from(mask)] = True
#
# fig2 = sns.heatmap(corr,mask = mask, linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
# fig2.figure.savefig("more_precise_correlation_table.png")
#
# ########################################################################################################################
#
# #Selecting candidates
# final2.drop(final2.columns[[0, 1, 2, 3, 5, 6, 9, 10, 11, 12, 13, 15 ]], axis = 1, inplace = True)
#
# # Check correlation between features
# sns.set(font_scale=3)
# colormap = plt.cm.magma
# plt.figure(figsize=(30,30))
#
# plt.title('Correlation of Selected Variables', y=1.05, size=50)
#
# corr = final2.astype(float).corr().round(2)
# mask = np.zeros_like(corr, dtype=bool)
#
# # mask upper diagonal of heatmap
# mask[np.triu_indices_from(mask)] = True
#
# fig3 = sns.heatmap(corr, mask = mask, linewidths=0.1,vmax=1.0, square=True, cmap=colormap,
#             linecolor='white', annot=True, annot_kws={"size": 50})
# fig3.figure.savefig("final_correlation_table.png")
#
#
# # In baseball, value over replacement player (or VORP) is a statistic popularized by Keith Woolner that
# # demonstrates how much a hitter or pitcher contributes to their team in comparison to a replacement-level
# # player who is an average fielder at that position and a below average hitter.
#
#
# # # Average points per game
# #
# # # Average turnovers per game
# #
# # # Defensive rebounds per game
# #
# # # overpaid underpaid  todo!!!
