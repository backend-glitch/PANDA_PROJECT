# panda basics

import pandas as pd
import numpy as np

# PART 1
data  ={

    "product" : ["pen","book","bag"],
    "price" : [10,250,500],
     "quantity" : [100,30,15]
}
df = pd.DataFrame(data)
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.describe())

#to select columns
print(df['product'])
print(df[['product','price']])

# to select rows
print(df.iloc[0])
print(df.iloc[0:2])

# to select specific columns with index.
print(df.loc[1])

# to filter
filter_1 = df[df['price'] > 100]
print(filter_1)

#to set and reset the index.
indexed = df.set_index('product')  # removes index column.
print(indexed)
#not_indexed = df.reset_index('product') # brings back index column.
#print(not_indexed)

# ADD COLOMNS 
df['total_value'] = df['price'] * df['quantity']

df['price' ] = df['price'] * 0.9

# to add it in table   #df.drop() : to remove something.
df  = df.drop('total_value',axis=1) #axis = 0 : to drop rows ,axis = 1 : to drop columns

# to add a columns
supplier = ['supplier a','supplier b','supplier c']
df['supplier'] = supplier

#to merge with other database.
additional_data = {
    'product' : ['pen','book',"bag"],
    'rating' : [4.5,4.8,4.7],
    'category' : ['statinary','education','accessories']
}
df_add = pd.DataFrame(additional_data)

df = pd.merge(df,df_add,left_on = "product",right_on ="product")
df = df.drop('product',axis = 1)

# to rename
df = df.rename(columns={
'product': 'product_name',
'price' : 'unit_price',
'quantity' : 'stock_quantity'
}
)
#to sort
df_sort = df.sort_values('unit_price')
print(df_sort)

#csv(comma separated values)
df_sort.to_csv("csv",index = False)
print("done")

# to load csv
df_1 = pd.read_csv('csv')
print(df_1)

#to clear existing csv
to_clear_csv = df.to_csv('inventory_database.csv', index=False)
print(to_clear_csv)

#PART2

# missing data
data_1 = {
    'Product Name': ['Pen', 'Book', 'Bag', 'Pencil'],
    'Unit Price': [9.0, 225.0, np.nan, 5.0],
    'Stock Quantity': [100, np.nan, 15, 50],# for no value : np.nan
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C', np.nan]
}

df_1 = pd.DataFrame(data_1)
print("DataFrame with Missing Data:")
print(df_1)

#detect missing data.
print("\nMissing Data Info:")
print(df_1.isnull())    # Shows True where data is missing and False for existing  value.
print("\nNumber of Missing Values per Column:")
print(df_1.isnull().sum()) # shows total value of missing values of each column.

#drop missing data.
df_drop = df_1.dropna()
print("\nAfter Dropping Rows with Missing Data:")
print(df_drop)

# to fill the missing data.
df_fill_num = df_1.fillna({
    'Unit Price': 0,
    'Stock Quantity': 0
})
print("\nAfter Filling Missing Numerical Data:")
print(df_fill_num)

# interpolate data
df_interpolate = df_1.interpolate()
print("\nAfter Interpolating Numerical Data:")
print(df_interpolate)


#PART3

# grouping and aggregate.
data_2 = {
    'Product Name': ['Pen', 'Book', 'Bag', 'Pencil', 'Notebook', 'Eraser'],
    'Unit Price': [9.0, 225.0, 450.0, 5.0, 150.0, 2.0],
    'Stock Quantity': [100, 30, 15, 50, 40, 200],
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier A', 'Supplier B', 'Supplier A'],
    'Category': ['Stationery', 'Education', 'Accessories', 'Stationery', 'Education', 'Stationery']
}

df_2= pd.DataFrame(data_2)
print("Initial DataFrame:")
print(df_2)

# to group by category.
grouped = df_2.groupby('Category').agg({
    'Stock Quantity': 'sum',
    'Unit Price': 'mean'
}).reset_index()

print("\nAggregated Data by Category:")
print(grouped)

# to group by row count.
count_supplier = df_2.groupby('Supplier')['Product Name'].count().reset_index()
count_supplier = count_supplier.rename(columns={'Product Name': 'Product Count'})

print("\nNumber of Products per Supplier:")
print(count_supplier)

# to have multiple aggregations .
agg_advanced = df_2.groupby('Category')['Stock Quantity'].agg(['sum', 'mean', 'max']).reset_index()
print("\nAdvanced Aggregation (sum, mean, max of Stock Quantity):")
print(agg_advanced)

