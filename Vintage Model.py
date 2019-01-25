import pandas as pd
import numpy as np

def frequency05(year):
    df = pd.read_csv("merge_2005.csv")

    OrigUnpPrinc=df["OrigUnpPrinc"]
    OrigDate=df["OrigDate"]
    ForeclosureDate=df["ForeclosureDate"]

    sum = 0
    Y1 = 0
    Y2 = 0
    Y3 = 0
    Y4 = 0
    Y5 = 0
    Y6 = 0
    for i in range(len(OrigDate)):
        a = OrigDate[i]
        if a[3:7] == year:
            if ForeclosureDate[i] == '0':
                sum += OrigUnpPrinc[i]
            else:
                b = ForeclosureDate[i]
                if b[6:10] < '2016':
                    if b[6:10] == str(year):
                        Y1 += OrigUnpPrinc[i]
                        sheet['Y1'][year] = '%.2f%%' % (Y1/sum * 100)
                    if b[6:10] == str(int(year) + 1):
                        Y2 += OrigUnpPrinc[i]
                        sheet['Y2'][year] = '%.2f%%' % (Y2/sum * 100)
                    if b[6:10] == str(int(year) + 2):
                        Y3 += OrigUnpPrinc[i]
                        sheet['Y3'][year] = '%.2f%%' % (Y3/sum * 100)
                    if b[6:10] == str(int(year) + 3):
                        Y4 += OrigUnpPrinc[i]
                        sheet['Y4'][year] = '%.2f%%' % (Y4/sum * 100)
                    if b[6:10] == str(int(year) + 4):
                        Y5 += OrigUnpPrinc[i]
                        sheet['Y5'][year] = '%.2f%%' % (Y5/sum * 100)
                    if b[6:10] == str(int(year) + 5):
                        Y6 += OrigUnpPrinc[i]
                        sheet['Y6'][year] = '%.2f%%' % (Y6/sum * 100)
    return
def frequency06(year):
    df = pd.read_csv("merge_2006.csv")

    OrigUnpPrinc=df["OrigUnpPrinc"]
    OrigDate=df["OrigDate"]
    ForeclosureDate=df["ForeclosureDate"]

    sum = 0
    Y1 = 0
    Y2 = 0
    Y3 = 0
    Y4 = 0
    Y5 = 0
    Y6 = 0
    for i in range(len(OrigDate)):
        a = OrigDate[i]
        if a[3:7] == year:
            if ForeclosureDate[i] == '0':
                sum += OrigUnpPrinc[i]
            else:
                b = ForeclosureDate[i]
                if b[6:10] < '2016':
                    if b[6:10] == str(year):
                        Y1 += OrigUnpPrinc[i]
                        sheet['Y1'][year] = '%.2f%%' % (Y1/sum * 100)
                    if b[6:10] == str(int(year) + 1):
                        Y2 += OrigUnpPrinc[i]
                        sheet['Y2'][year] = '%.2f%%' % (Y2/sum * 100)
                    if b[6:10] == str(int(year) + 2):
                        Y3 += OrigUnpPrinc[i]
                        sheet['Y3'][year] = '%.2f%%' % (Y3/sum * 100)
                    if b[6:10] == str(int(year) + 3):
                        Y4 += OrigUnpPrinc[i]
                        sheet['Y4'][year] = '%.2f%%' % (Y4/sum * 100)
                    if b[6:10] == str(int(year) + 4):
                        Y5 += OrigUnpPrinc[i]
                        sheet['Y5'][year] = '%.2f%%' % (Y5/sum * 100)
                    if b[6:10] == str(int(year) + 5):
                        Y6 += OrigUnpPrinc[i]
                        sheet['Y6'][year] = '%.2f%%' % (Y6/sum * 100)
    return
def frequency07(year):
    df = pd.read_csv("merge_2007.csv")

    OrigUnpPrinc=df["OrigUnpPrinc"]
    OrigDate=df["OrigDate"]
    ForeclosureDate=df["ForeclosureDate"]

    sum = 0
    Y1 = 0
    Y2 = 0
    Y3 = 0
    Y4 = 0
    Y5 = 0
    Y6 = 0
    for i in range(len(OrigDate)):
        a = OrigDate[i]
        if a[3:7] == year:
            if ForeclosureDate[i] == '0':
                sum += OrigUnpPrinc[i]
            else:
                b = ForeclosureDate[i]
                if b[6:10] < '2016':
                    if b[6:10] == str(year):
                        Y1 += OrigUnpPrinc[i]
                        sheet['Y1'][year] = '%.2f%%' % (Y1/sum * 100)
                    if b[6:10] == str(int(year) + 1):
                        Y2 += OrigUnpPrinc[i]
                        sheet['Y2'][year] = '%.2f%%' % (Y2/sum * 100)
                    if b[6:10] == str(int(year) + 2):
                        Y3 += OrigUnpPrinc[i]
                        sheet['Y3'][year] = '%.2f%%' % (Y3/sum * 100)
                    if b[6:10] == str(int(year) + 3):
                        Y4 += OrigUnpPrinc[i]
                        sheet['Y4'][year] = '%.2f%%' % (Y4/sum * 100)
                    if b[6:10] == str(int(year) + 4):
                        Y5 += OrigUnpPrinc[i]
                        sheet['Y5'][year] = '%.2f%%' % (Y5/sum * 100)
                    if b[6:10] == str(int(year) + 5):
                        Y6 += OrigUnpPrinc[i]
                        sheet['Y6'][year] = '%.2f%%' % (Y6/sum * 100)
    return
def frequency08(year):
    df = pd.read_csv("merge_2008.csv")

    OrigUnpPrinc=df["OrigUnpPrinc"]
    OrigDate=df["OrigDate"]
    ForeclosureDate=df["ForeclosureDate"]

    sum = 0
    Y1 = 0
    Y2 = 0
    Y3 = 0
    Y4 = 0
    Y5 = 0
    Y6 = 0
    for i in range(len(OrigDate)):
        a = OrigDate[i]
        if a[3:7] == year:
            if ForeclosureDate[i] == '0':
                sum += OrigUnpPrinc[i]
            else:
                b = ForeclosureDate[i]
                if b[6:10] < '2016':
                    if b[6:10] == str(year):
                        Y1 += OrigUnpPrinc[i]
                        sheet['Y1'][year] = '%.2f%%' % (Y1/sum * 100)
                    if b[6:10] == str(int(year) + 1):
                        Y2 += OrigUnpPrinc[i]
                        sheet['Y2'][year] = '%.2f%%' % (Y2/sum * 100)
                    if b[6:10] == str(int(year) + 2):
                        Y3 += OrigUnpPrinc[i]
                        sheet['Y3'][year] = '%.2f%%' % (Y3/sum * 100)
                    if b[6:10] == str(int(year) + 3):
                        Y4 += OrigUnpPrinc[i]
                        sheet['Y4'][year] = '%.2f%%' % (Y4/sum * 100)
                    if b[6:10] == str(int(year) + 4):
                        Y5 += OrigUnpPrinc[i]
                        sheet['Y5'][year] = '%.2f%%' % (Y5/sum * 100)
                    if b[6:10] == str(int(year) + 5):
                        Y6 += OrigUnpPrinc[i]
                        sheet['Y6'][year] = '%.2f%%' % (Y6/sum * 100)
    return
def frequency09(year):
    df = pd.read_csv("merge_2009.csv")

    OrigUnpPrinc=df["OrigUnpPrinc"]
    OrigDate=df["OrigDate"]
    ForeclosureDate=df["ForeclosureDate"]

    sum = 0
    Y1 = 0
    Y2 = 0
    Y3 = 0
    Y4 = 0
    Y5 = 0
    Y6 = 0
    for i in range(len(OrigDate)):
        a = OrigDate[i]
        if a[3:7] == year:
            if ForeclosureDate[i] == '0':
                sum += OrigUnpPrinc[i]
            else:
                b = ForeclosureDate[i]
                if b[6:10] < '2016':
                    if b[6:10] == str(year):
                        Y1 += OrigUnpPrinc[i]
                        sheet['Y1'][year] = '%.2f%%' % (Y1/sum * 100)
                    if b[6:10] == str(int(year) + 1):
                        Y2 += OrigUnpPrinc[i]
                        sheet['Y2'][year] = '%.2f%%' % (Y2/sum * 100)
                    if b[6:10] == str(int(year) + 2):
                        Y3 += OrigUnpPrinc[i]
                        sheet['Y3'][year] = '%.2f%%' % (Y3/sum * 100)
                    if b[6:10] == str(int(year) + 3):
                        Y4 += OrigUnpPrinc[i]
                        sheet['Y4'][year] = '%.2f%%' % (Y4/sum * 100)
                    if b[6:10] == str(int(year) + 4):
                        Y5 += OrigUnpPrinc[i]
                        sheet['Y5'][year] = '%.2f%%' % (Y5/sum * 100)
                    if b[6:10] == str(int(year) + 5):
                        Y6 += OrigUnpPrinc[i]
                        sheet['Y6'][year] = '%.2f%%' % (Y6/sum * 100)
    return
def frequency10(year):
    df = pd.read_csv("merge_2010.csv")

    OrigUnpPrinc=df["OrigUnpPrinc"]
    OrigDate=df["OrigDate"]
    ForeclosureDate=df["ForeclosureDate"]

    sum = 0
    Y1 = 0
    Y2 = 0
    Y3 = 0
    Y4 = 0
    Y5 = 0
    Y6 = 0
    for i in range(len(OrigDate)):
        a = OrigDate[i]
        if a[3:7] == year:
            if ForeclosureDate[i] == '0':
                sum += OrigUnpPrinc[i]
            else:
                b = ForeclosureDate[i]
                if b[6:10] < '2016':
                    if b[6:10] == str(year):
                        Y1 += OrigUnpPrinc[i]
                        sheet['Y1'][year] = '%.2f%%' % (Y1/sum * 100)
                    if b[6:10] == str(int(year) + 1):
                        Y2 += OrigUnpPrinc[i]
                        sheet['Y2'][year] = '%.2f%%' % (Y2/sum * 100)
                    if b[6:10] == str(int(year) + 2):
                        Y3 += OrigUnpPrinc[i]
                        sheet['Y3'][year] = '%.2f%%' % (Y3/sum * 100)
                    if b[6:10] == str(int(year) + 3):
                        Y4 += OrigUnpPrinc[i]
                        sheet['Y4'][year] = '%.2f%%' % (Y4/sum * 100)
                    if b[6:10] == str(int(year) + 4):
                        Y5 += OrigUnpPrinc[i]
                        sheet['Y5'][year] = '%.2f%%' % (Y5/sum * 100)
                    if b[6:10] == str(int(year) + 5):
                        Y6 += OrigUnpPrinc[i]
                        sheet['Y6'][year] = '%.2f%%' % (Y6/sum * 100)
    return


sheet = pd.DataFrame(columns=['Y1','Y2','Y3','Y4','Y5','Y6'],index=['2005','2006','2007','2008','2009','2010','Average'])

frequency05('2005')
frequency06('2006')
frequency07('2007')
frequency08('2008')
frequency09('2009')
frequency10('2010')

print(sheet)
sheet.to_csv('true loss rate.csv')
