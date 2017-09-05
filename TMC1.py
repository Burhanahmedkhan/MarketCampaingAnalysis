import pandas as pd
import dbapi
import pyhdb
import pandas as pd


connection = pyhdb.connect(
    host="10.118.0.82",
    port=30015,
    user="paripatel",
    password="Winter2015"
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

dff['SALE_DOLLARS'].value_counts().plot(color='red',grid = True)

dff['SALE_DOLLARS'].value_counts().plot(kind='kde',color='red',grid = True)


category_plot = dff['CATEGORY_NAME'].value_counts().plot.bar(grid=True,alpha = 0.3,rot=80,
                                             title="Popularity of Category").set_xlabelll

vendor_plot = dff['VENDOR_NAME'].value_counts().plot.bar(grid=True,alpha = 0.3,rot=80,
                                             title="Popularity of Category")
dff['VENDOR_NAME'].value_counts()

df1 = dff.groupby(['ITEM_DESCRIPTION', 'SALE_DOLLARS'])['ITEM_DESCRIPTION'].count().unstack('SALE_DOLLARS')
price_plot = df1.plot(kind='bar', stacked=False, grid=True,alpha = 0.7,rot=80,
                                             title="Prices of different Brands")
price_plot.set_xlabel("ITEM_DESCRIPTION")
price_plot.set_ylabel("SALE_DOLLARS")


df2 = dff.groupby(['VENDOR_NAME', 'ZIP_CODE'])['VENDOR_NAME'].count().unstack('ZIP_CODE')
price_plot2 = df2.plot(kind='bar', stacked=False, grid=True,alpha = 0.7,rot=80,
                                             title="Location of different Vendors")
price_plot2.set_xlabel("Brands")
price_plot2.set_ylabel("ZIP_CODE")


