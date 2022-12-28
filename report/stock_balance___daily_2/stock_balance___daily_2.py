# Copyright (c) 2022, DT team and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data()
	return columns, data

def get_columns():
	columns = [
		{
			"label": ("Item"),
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"width": 100,
		},
		{
			"label": ("Company"), 
			"fieldname": "company", 
			"width": 150
			
		},
		{
			"label": ("Warehouse"),
			"fieldname": "warehouse",
			"fieldtype": "Link",
			"options": "Warehouse",
			"width": 200,
		},
        
	]

	for date in range(1,31):
		col_date = {
			"label":("Day_"+ date) ,
			"fieldname":("day_"+ date),
			"fieldtype": "Data",
			"width" : 150,
		}
		columns.append(col_date)
	return columns

def get_data():
	