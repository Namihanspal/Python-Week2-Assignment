
#NECESSARY IMPORTSS

import csv

def get_option():  

  ''' Displays the recommendation options and description, takes in the user entered option  '''

  print("\n")
  print("======= Welcome to canteen reco system ==========\n")
  print("Your options are\n")
  print("1. Show the available canteens")
  print("2. Help me select a canteen")
  print("3. Exit\n")

  while True:
      try:
          option = int(input("Enter your option "))
          if option not in [1,2,3]:
              raise Exception("Kindly enter the options in the menu")
          break

      except Exception as ex:
          print(ex)

  return option


def get_desired_result(option,canteens,price_range):

  ''' For the entered option the relevant results are generated (tuple of option and results) '''

  if option==1:
    return (option,canteens)

  elif option==2:
    while True:
      try:

        money=int(input('Enter your budget '))
        if money<0:
          raise Exception('Kindly enter a positive amount')
        break

      except Exception as ex:
        print(ex)

    return (option,[(canteen,price) for canteen,price in zip(canteens,price_range) if money>price[0] and money<price[1]])

  elif option==3:
    exit(0)
   
    
def show_results(option,results):

  ''' Results corresponding to the options are printed'''

  print("\n")

  if option==1:
    print('The available canteens are as below:\n')
    for canteen in results:      
      print(canteen)      

  elif option==2:
    if len(results)!=0:
      print("The available canteens and their price range are as below:\n")
    else:
      print('Sorry no results :( \n')      
    for canteen,price_range in results:
      print('{0} has price ranging from {1} to {2} fitting your budget'.format(canteen,price_range[0],price_range[1]))


def main():

  #Read in the data from csv into lists, canteens_lst - list of canteens and price_range_lst - list of tuples of price range
  canteens_lst = []
  price_range_lst=[]
  with open('Input.csv','r') as csv_file:
      csv_reader=csv.reader(csv_file, delimiter=',')
      next(csv_reader, None)  
      for row in csv_reader:
          canteens_lst.append(row[0])
          price_range_lst.append((int(row[1]),int(row[2])))

  # An infinte loop is created to invoke different options from the user unless option 3 is selected, which exits the loop
  while True:  
    option = get_option()
    option,results=get_desired_result(option,canteens_lst,price_range_lst)
    show_results(option,results)
  

if __name__ == "__main__":
    main()

