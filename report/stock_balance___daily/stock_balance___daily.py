# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

# from operator import itemgetter
# from typing import Any, Dict, List, Optional, TypedDict

import frappe
# from frappe import _
# from frappe.query_builder.functions import CombineDatetime
# from frappe.utils import cint, date_diff, flt, getdate
# from frappe.utils.nestedset import get_descendants_of

# import erpnext
# from erpnext.stock.doctype.inventory_dimension.inventory_dimension import get_inventory_dimensions
# from erpnext.stock.doctype.warehouse.warehouse import apply_warehouse_filter
# from erpnext.stock.report.stock_ageing.stock_ageing import FIFOSlots, get_average_age
# from erpnext.stock.utils import add_additional_uom_columns, is_reposting_item_valuation_in_progress


# class StockBalanceFilter(TypedDict):
# 	company: Optional[str]
# 	from_date: str
# 	to_date: str
# 	item_group: Optional[str]
# 	item: Optional[str]
# 	date: str
# 	voucher_type: Optional[str]
# 	warehouse: Optional[str]
# 	warehouse_type: Optional[str]
# 	include_uom: Optional[str]  # include extra info in converted UOM
# 	show_stock_ageing_data: bool
# 	show_variant_attributes: bool


# SLEntry = Dict[str, Any]


def execute(filters: Optional[StockBalanceFilter] = None):
    columns = get_columns()
    data = get_data()
    return columns, data

def get_columns():
    columns = [
		{
			"label": _("Item"),
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"width": 100,
		},
		{"label": _("Company"), "fieldname": "company", "width": 150},
		# {
		# 	"label": _("Voucher Type"),
		# 	"fieldname": "voucher_type",
		# 	# "fieldtype": "Link",
		# 	"options": "Data",
		# 	"width": 200,
		# },
		{
			"label": _("Warehouse"),
			"fieldname": "warehouse",
			"fieldtype": "Link",
			"options": "Warehouse",
			"width": 200,
		},
        {
			"label": _("Day 1"),
			"fieldname": "day_1",
			"fieldtype": "Data",
			"width": 100,
		},
        {
			"label": _("Day 2"),
			"fieldname": "day_2",
			"fieldtype": "Data",
			"width": 100,
		},
        # {
		# 	"label": _("Day 3"),
		# 	"fieldname": "day_3",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
        # {
		# 	"label": _("Day 4"),
		# 	"fieldname": "day_4",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
        # {
		# 	"label": _("Day 5"),
		# 	"fieldname": "day_5",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
        # {
		# 	"label": _("Day 6"),
		# 	"fieldname": "day_6",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
        # {
		# 	"label": _("Day 7"),
		# 	"fieldname": "day_7",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
        # {
		# 	"label": _("Day 8"),
		# 	"fieldname": "day_8",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
        # {
		# 	"label": _("Day 9"),
		# 	"fieldname": "day_9",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
        # {
		# 	"label": _("Day 10"),
		# 	"fieldname": "day_10",
		# 	"fieldtype": "Data",
		# 	"width": 100,
		# },
	]
    return columns


# def get_data():
# 	sle= 'Stock Ledger Entry'
# 	d_data = frappe.get_list(sle, pluck = 'posting_date')
# 	data =[]
# 	for d in d_data:
# 		row = {'day_1': d}
# 		data.append(row)
# 	item_data = frappe.get_list(sle, pluck = 'item')
# 	for d in item_data:
# 		if not (any (i['item_code']== d for i in data )):
# 			row = {'item_code': d}
# 			data.append(row)
# 	return data

def get_data():
	d_data = frappe.get_all(doctype = "Stock Ledger Entry",fields = ['item_code', 'warehouse','posting_date','voucher_type','company','actual_qty'])
	data =[]
	for d in d_data:
		row = {
			'item_code': d.item_code,
			'company': d.company,
			'warehouse': d.warehouse,
			# 'voucher_type':d.voucher_type,
			# 'day_2':d.voucher_type,
			'day_1': int(d.actual_qty)
		}
		# if str(d.posting_date) == '2022-12-05':
		# 	row['day_1'] += int(d.actual_qty)
		# data = check(row,d_data,data)
		if str(d.posting_date) != '2022-12-05':
			continue 
		flag = 1
		for dic in data:       
			if (row["item_code"] == dic["item_code"]) & (row["warehouse"] == dic["warehouse"]) & (row["company"] == dic["company"]):
				flag = 0
				dic['day_1'] += row['day_1']
		if flag == 1:
			data.append(row)
	
	# for ls in data:
	# 	for s in d_data:
	# 		if (str(s.item_code) and str(s.warehouse)) in ls.values():
	# 			if str(s.posting_date) =='2022-12-05' :
	# 				ls['day_1'] += 's'
			# data.append(row)
	
	return data

# def check (row,data,master):
# 	flag = 1
# 	for line_dic in data:
# 		if row == line_dic:
# 			flag = 0
# 	if flag == 1:
# 		master.append(row)
# 	return master