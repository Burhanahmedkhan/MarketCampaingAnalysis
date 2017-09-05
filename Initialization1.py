Python 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:25:24) [MSC v.1900 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.



%clear


import pandas as pd
import dbapi
import pyhdb
import pandas as pd

connection = pyhdb.connect(
    host="",
    port=,
    user="",
    password=""
)

cursor = connection.cursor()
connection.isconnected()
statement = "SELECT TOP 1000 * FROM PARIPATEL.LIQUOR_SALES"
cursor.execute(statement)
dff= pd.DataFrame(cursor.fetchall())
cursor.rowcount
connection.close()

dff.columns=['INVOICE_NUMBER',
'DATE',
'STORE_NUMBER',
'STORE_NAME',
'ADDRESS',
'CITY',
'ZIP_CODE',
'STORE_LOCATION',
'COUNTY_NUMBER',
'COUNTY',
'CATEGORY',
'CATEGORY_NAME',
'VENDOR_NUMBER',
'VENDOR_NAME',
'ITEM_NUMBER',
'ITEM_DESCRIPTION',
'PACK',
'BOTTLE_VOLUME',
'STATE_BOTTLE_COST',
'STATE_BOTTLE_RETAIL',
'BOTTLES_SOLD',
'SALE_DOLLARS',
'VOLUME_SOLD_LITERS',
'VOLUME_SOLD_GALLONS',
'SALES_DATE']

pd.isnull(dff).sum()
Out[6]: 
INVOICE_NUMBER         0
DATE                   0
STORE_NUMBER           0
STORE_NAME             0
ADDRESS                0
CITY                   0
ZIP_CODE               0
STORE_LOCATION         0
COUNTY_NUMBER          0
COUNTY                 0
CATEGORY               0
CATEGORY_NAME          0
VENDOR_NUMBER          0
VENDOR_NAME            0
ITEM_NUMBER            0
ITEM_DESCRIPTION       0
PACK                   0
BOTTLE_VOLUME          0
STATE_BOTTLE_COST      0
STATE_BOTTLE_RETAIL    0
BOTTLES_SOLD           0
SALE_DOLLARS           0
VOLUME_SOLD_LITERS     0
VOLUME_SOLD_GALLONS    0
SALES_DATE             0
dtype: int64

dff['SALE_DOLLARS'].value_counts().plot(color='red',grid = True)
Out[7]: <matplotlib.axes._subplots.AxesSubplot at 0x198e1565ba8>
￼

dff['SALE_DOLLARS'].value_counts().plot(kind='kde',color='red',grid = True)
Out[8]: <matplotlib.axes._subplots.AxesSubplot at 0x198e1b03e80>
￼

category_plot = dff['CATEGORY_NAME'].value_counts().plot.bar(grid=True,alpha = 0.3,rot=80,
                                             title="Popularity of Category").set_xlabelll
Traceback (most recent call last):

  File "<ipython-input-9-a4ff98556a4d>", line 2, in <module>
    title="Popularity of Category").set_xlabelll

AttributeError: 'AxesSubplot' object has no attribute 'set_xlabelll'


￼

vendor_plot = dff['VENDOR_NAME'].value_counts().plot.bar(grid=True,alpha = 0.3,rot=80,
                                             title="Popularity of Vendor")

￼

dff['VENDOR_NAME'].value_counts()
Out[11]: 
Diageo Americas                     658
Jim Beam Brands                     195
Proximo                              45
Luxco-St Louis                       33
Pernod Ricard USA/Austin Nichols     30
Constellation Wine Company, Inc.     23
Stoli Group                          13
Imperial Brands, Inc.                 3
Name: VENDOR_NAME, dtype: int64

df1 = dff.groupby(['ITEM_DESCRIPTION', 'SALE_DOLLARS'])['ITEM_DESCRIPTION'].count().unstack('SALE_DOLLARS')

price_plot = df1.plot(kind='bar', stacked=False, grid=True,alpha = 0.7,rot=80,
                                             title="Prices of different Brands")
price_plot.set_xlabel("ITEM_DESCRIPTION")
price_plot.set_ylabel("SALE_DOLLARS")
Out[13]: <matplotlib.text.Text at 0x198e30defd0>
￼


df2 = dff.groupby(['VENDOR_NAME', 'ZIP_CODE'])['VENDOR_NAME'].count().unstack('ZIP_CODE')

price_plot2 = df2.plot(kind='bar', stacked=False, grid=True,alpha = 0.7,rot=80,
                                             title="Location of different Vendors")
price_plot2.set_xlabel("Brands")
price_plot2.set_ylabel("ZIP_CODE")
Out[15]: <matplotlib.text.Text at 0x198e2ebd860>
￼
