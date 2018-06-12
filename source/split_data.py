import pandas as pd
import numpy as np
import random
random.seed(0)


def split_customers(df,cust_key='CUSTOMER_EXT_ID',n=5):
	
	'''
	Splits customers into n groups	
	input: 
		df: dataframe,
		cust_key: key to split on, 
		n: number of groups to split into
	returns:
		a list of n lists
	'''
	
	customers = df[cust_key].unique()
	random.shuffle(customers)
	groups = np.array_split(customers,n)
	return groups

def split_to_dict(groups):

	'''
	returns a dictionary to map each ID to split on (CUSTOMER_EXT_ID) to its group
	'''

	return {j:i for i,group in enumerate(groups) for j in group}


def assign_group(df,group_dict,cust_key='CUSTOMER_EXT_ID',group_key='split_group_i'):

	'''
	assigns groups to each customer as per the group split. facilitates groupby-ing
	'''
	df[group_key] = df[cust_key].apply(lambda i:group_dict[i])
	return df

def split_ids(df,cust_key='CUSTOMER_EXT_ID',n=5,group_key='split_group_i'):
	
	'''
	Function that puts all other functions together, the only one to be used externally
	'''

	groups = split_customers(df,cust_key,n)
	group_dict = split_to_dict(groups)
	df = assign_group(df,group_dict,cust_key)
	return df












