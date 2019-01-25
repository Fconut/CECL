import pandas as pd
import numpy as np

acquisition = ['LoanID','Channel','SellerName','OrigInterestRate','OrigUnpPrinc','OrigLoanTerm',
               'OrigDate','FirstPayment','OrigLTV','OrigCLTV','NumBorrow','DTIRat','CreditScore',
               'FTHomeBuyer','LoanPurpose','PropertyType','NumUnits','OccStatus','PropertyState',
               'Zip','MortInsPerc','ProductType','CoCreditScore','MortInsType','RelMortInd'];
performance = ['LoanID','MonthRep','Servicer','CurrInterestRate','CurActUnpBal','LoanAge',
               'MonthsToMaturity','AdMonthsToMaturity','MaturityDate','MSA','CLDS','ModFlag',
               'ZeroBalCode','ZeroBalDate','LastInstallDate','ForeclosureDate','DispositionDate',
               'PPRC','AssetRecCost','MHRC','ATFHP','NetSaleProceeds','CreditEnhProceeds','RPMWP',
               'OFP','NIBUPB','PFUPB','RMWPF','FPWA','ServicingIndicator'];

df_acq = pd.read_csv('Acquisition_2007Q2.txt', sep='|', names=acquisition, index_col=False)
df_per = pd.read_csv('Performance_2007Q2.txt', sep='|', names=performance, index_col=False)

df_per = df_per[['LoanID','Servicer','CurrInterestRate','CurActUnpBal','LoanAge','MonthsToMaturity','ForeclosureDate']].reset_index(drop=True)
df_per.drop_duplicates(subset=['LoanID'], keep='last', inplace=True)

df = pd.merge(df_acq, df_per, on='LoanID')
df.drop('LoanID', axis=1, inplace=True)
df.rename(index=str, columns={"ForeclosureDate": 'Default'}, inplace=True)

df['Default'].fillna(0, inplace=True)
df.loc[df['Default'] != 0, 'Default'] = 1
df['Default'] = df['Default'].astype(int)

df_null = pd.DataFrame({'Count': df.isnull().sum(), 'Percent': 100*df.isnull().sum()/len(df)})
print(df_null[df_null['Count'] > 0])

'''
Normally, if the percentage of nulls was small (say less than 10% or so), I would try
to fill them in using the column mean, median, or mode, or I would try to predict their
values using a machine learning algorithm. However, since the our dataset is so large,
we can drop the null rows entirely without much consequence.
'''

df.drop(['MortInsPerc','CoCreditScore','MortInsType','Servicer'], axis=1, inplace=True)
df.dropna(inplace=True)

df.drop('ProductType', axis=1, inplace=True)

df.to_csv('merge.csv')
