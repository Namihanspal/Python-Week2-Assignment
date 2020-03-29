

#

def take_input():

# '''

# This function takes in input for the input
# Checks for the various exceptions in the input

# '''

	while True:
		try:
			req_num = int(input('Enter the number '))
			if req_num > 1000:
				raise Exception('Too much money man, the canteen budget is not that high')
			return req_num	
				
		except Exception as inst:
				print(inst)

			

def canteens(money):

	# """

	# This function has the details of canteens and their respective prices
	# It dynamically returns the list of canteens which suits the user's budget

	# """

	canteen_lst= ['canteen1','canteen2','canteen3','canteen4','canteen5']
	price_range=[(10,30),(40,70),(20,50),(100,200),(1,600)]

	req_lst = []
	for canteen,price_range in zip(canteen_lst,price_range):
		if money>price_range[0] and money <price_range[1]:
			req_lst.append((canteen,price_range))
	# return req_lst		

	# print('The elements from the req_lst is below')
	# print(req_lst[0])
	# req_lst = [canteen,price_range canteen,price_range in zip(canteen_lst,price_range) if money > price_range[0] and money < price_range[1]]		
	return req_lst


def return_pretty(req_lst):


	# """
	
	# Does all the pretty formatting and displays the results


	# """
	for item in req_lst:
		print('{0} with lowest price {1} and highest price {2} fits your budget'.format(item[0],item[1][0],item[1][1]))


def main():
	money = take_input()	
	req_canteens=canteens(money)
	return_pretty(req_canteens)

if __name__ == "__main__":
	main()





