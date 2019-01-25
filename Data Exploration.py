import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mp

df = pd.read_csv("merge.csv")

fig, axes = mp.subplots(nrows=1, ncols=1, figsize=(8,6))

ax = df['Default'].value_counts().divide(len(df)).plot.bar(width=0.9, rot=0)
ax.set_xlabel('Default')
ax.set_ylabel('Number of Borrowers')
ax.set_ylim(0,1)
mp.show()

fig, axes = mp.subplots(nrows=1, ncols=2, figsize=(16,6))

ax = df.groupby('Default')['OrigInterestRate'].plot.hist(bins=30, density=True, alpha=0.25, ax=axes[0])
ax[0].set_ylabel('Normalized Frequency')
ax[0].set_xlabel('OrigInterestRate')
ax[0].legend()

ax = df.boxplot(by='Default', column='OrigInterestRate', grid=False, widths=(0.8, 0.8), ax=axes[1])
ax.set_ylabel('OrigInterestRate')
ax.set_ylim(0,10)
ax.set_title('')
fig.suptitle('')
mp.show()

fig, axes = mp.subplots(nrows=1, ncols=2, figsize=(16,6))

ax = df['NumBorrow'].value_counts().divide(len(df)).plot.bar(width=0.9, ax=axes[0], rot=0)
ax.set_xlabel('NumBorrow')
ax.set_ylabel('Number of Borrowers')
ax.set_ylim(0,1)

xtab = pd.pivot_table(df, index='Default', columns='NumBorrow', aggfunc='size')
xtab = xtab.div(xtab.sum(axis=1), axis=0)
ax = xtab.plot.barh(stacked=True, width=0.9, ax=axes[1])

ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
ax.set_xlabel('Fraction of Borrowers')
ax.set_ylabel('Default')
ax.set_xlim(0,1)
mp.show()

fig, axes = mp.subplots(nrows=1, ncols=2, figsize=(16,6))

ax = df.groupby('Default')['DTIRat'].plot.hist(bins=30, density=True, alpha=0.25, ax=axes[0])
ax[0].set_ylabel('Normalized Frequency')
ax[0].set_xlabel('DTIRat')
ax[0].legend()

ax = df.boxplot(by='Default', column='DTIRat', grid=False, widths=(0.8, 0.8), ax=axes[1])
ax.set_ylabel('DTIRat')
ax.set_title('')
fig.suptitle('')
mp.show()

fig, axes = mp.subplots(nrows=1, ncols=2, figsize=(16,6))

ax = df.groupby('Default')['CreditScore'].plot.hist(bins=30, density=True, alpha=0.25, ax=axes[0])
ax[0].set_ylabel('Normalized Frequency')
ax[0].set_xlabel('CreditScore')
ax[0].legend()

ax = df.boxplot(by='Default', column='CreditScore', grid=False, widths=(0.8, 0.8), ax=axes[1])
ax.set_ylabel('CreditScore')
ax.set_title('')
fig.suptitle('')
mp.show()

data = df[df['Zip'].isin(df['Zip'].value_counts().index.tolist()[:10])]

xtab = pd.pivot_table(data, index='Zip', columns='Default', aggfunc='size')
xtab = xtab.div(xtab.sum(axis=1), axis=0)
ax = xtab.plot.barh(stacked=True, width=0.9, figsize=(8,6))

ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
ax.set_xlabel('Fraction of Borrowers')
ax.set_ylabel('ZIP Code')
ax.set_xlim(0,1)
mp.show()

fig, axes = mp.subplots(figsize=(10,8))

sns.heatmap(np.round(df.corr(), 2), annot=True, cmap='bwr', vmin=-1, vmax=1, square=True, linewidths=0.5)
mp.show()

fig, axes = mp.subplots(nrows=1, ncols=2, figsize=(16,6))

df.dropna().sample(n=1000).plot.scatter(x='OrigLTV', y='OrigCLTV', ax=axes[0])
df.dropna().sample(n=1000).plot.scatter(x='CurActUnpBal', y='OrigUnpPrinc', ax=axes[1])
mp.show()


df.drop(['OrigCLTV','OrigUnpPrinc'], axis=1, inplace=True)

df.reset_index(drop=True, inplace=True)

df['OrigDateMonth'] = df['OrigDate'].apply(lambda x: x.split('/')[0].strip()).astype(object)
df['OrigDateYear'] = df['OrigDate'].apply(lambda x: x.split('/')[1].strip()).astype(object)

df['FirstMonth'] = df['FirstPayment'].apply(lambda x: x.split('/')[0].strip()).astype(object)
df['FirstYear'] = df['FirstPayment'].apply(lambda x: x.split('/')[1].strip()).astype(object)

df.drop(['OrigDate','FirstPayment'], axis=1, inplace=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)

df.to_csv('new_merge.csv')
