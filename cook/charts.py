from chartjs.views.lines import BaseLineChartView
from .models import Category, Product, WaiterOrder

class DishChartJSONView(BaseLineChartView):
	def get_providers(self):
		list = []
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			list.append(dish)
		return list

	def get_labels(self):
		list = []
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			list.append(dish)
		return [['',],]

	def get_data(self):
		"""Return 3 datasets to plot."""
		
		list = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			if dish in map : map[dish] =+ task.count
			else : map[dish] = task.count
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			list.append([map[dish],])
		return list	

class CategoryChartJSONView1(BaseLineChartView):

	def get_labels(self):
		list = []
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			list.append(dish)
		return list


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		list = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			if dish in map : map[dish] =+ task.count
			else : map[dish] = task.count
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			list.append(map[dish])
		return [list,]	

class CategoryChartJSONView(BaseLineChartView):

	def get_labels(self):
		list = []
		for prod in Category.objects.all():
			list.append(prod.category_name)
		return list


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		list2 = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			cat = task.dish.category.category_name
			if cat in map : map[cat] =+ task.count
			else : map[cat] = task.count
		
		for category in Category.objects.all():
			try:
				el = map[category.category_name]
				list2.append(el)
			except KeyError:
				list2.append(0)
		return [list2]		

class CategoryChartJSONView2(BaseLineChartView):

	def get_labels(self):
		list = []
		for prod in Category.objects.all():
			list.append(prod.category_name)
		return list


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		list2 = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			cat = task.dish.category.category_name
			if cat in map : map[cat] =+ task.price_default
			else : map[cat] = task.price_default
		
		for category in Category.objects.all():
			try:
				el = map[category.category_name]
				list2.append(el)
			except KeyError:
				list2.append(0)
		return [list2]
dish_chart_json = DishChartJSONView.as_view()		
category_chart_json = CategoryChartJSONView.as_view()
category_chart_json1 = CategoryChartJSONView1.as_view()
category_chart_json2 = CategoryChartJSONView2.as_view()