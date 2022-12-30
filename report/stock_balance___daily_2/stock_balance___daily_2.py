# Copyright (c) 2022, DT team and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data()
	return columns, data

d_data = frappe.get_all(doctype = "Stock Ledger Entry",fields = ['item_code', 'warehouse','posting_date','voucher_type','company','actual_qty'], order_by = 'posting_date asc')

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
	# for date in range(1,31):
	# 	col_date = {
	# 		"label":("Day_"+ str(date)) ,
	# 		"fieldname":("day_"+ str(date)),
	# 		"fieldtype": "Data",
	# 		"width" : 150,
	# 	}
	# 	columns.append(col_date)

	for d in d_data:
		col_date = {
			"label" : str(d.posting_date),
			"fieldname": str(d.posting_date),
			"fieldtype": "Data",
			"width" : 150,
		}
		for c in columns:
			flag = 0
			if c["label"] == col_date["label"]:
				flag = 1
		if flag ==  0:
			columns.append(col_date)
	


	return columns

def get_data():
	
	data =[]
	
	for d in d_data:
		# day = str(int((str(d.posting_date))[8:]))
		row = {
			'item_code': d.item_code,
			'company': d.company,
			'warehouse': d.warehouse,
			# ('day_'+ day): d.actual_qty,
			str(d.posting_date): d.actual_qty
		}
		flag = 1
		for dic in data:       
			if (row["item_code"] == dic["item_code"]) & (row["warehouse"] == dic["warehouse"]) & (row["company"] == dic["company"]):
				flag = 0
				if str(d.posting_date) not in dic.keys():
					dic[str(d.posting_date)] = row[str(d.posting_date)]
				else:
					dic[str(d.posting_date)] += row[str(d.posting_date)]
		if flag == 1:
			data.append(row)
	return data
