import pandas as pd
import sys
sys.path.insert(0,'source/')
from split_data import *

def test_splits():
	'''
	assign_group
	split_customers
	split_to_dict
	'''
	
	datafile = 'data/'
	filename = 'file_test.csv'
	data = '%s%s' % (datafile,filename)
	df = pd.read_csv(data,sep=';')
	n = 5
	group_key='split_group_i'

	groups = split_customers(df,n=n)
	empty_groups = filter(lambda i:len(i) == 0 , groups )
	group_dict = split_to_dict(groups)
	df = assign_group(df,group_dict)

	assert len(groups) == n
	assert not empty_groups
	assert list(set(group_dict.values())) == range(n)
	assert set(df[group_key].unique().tolist()) == set(range(n))


if __name__ == "__main__":
    test_splits()