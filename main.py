from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#  test comment for push
MenuVar = Menu()
CoffeeMakerVar = CoffeeMaker()
MoneyMachineVar = MoneyMachine()


def user_input_function():
    userinput = input(f'Please select a drink {MenuVar.get_items()}: ')
    return userinput


#                               parse user input

def final_function():
    loop_on = True
    while loop_on:
        userinput = user_input_function()
        if userinput == "report":
            print(CoffeeMakerVar.report())
        elif userinput == "profit":
            print(MoneyMachineVar.profit)
        else:

            # get MenuItem object
            MenuItemObjectReturn = MenuVar.find_drink(order_name=userinput)
            # parse returned MenuItem object and return is resource sufficient bool
            IsResourceSufficient = CoffeeMakerVar.is_resource_sufficient(MenuItemObjectReturn)
            # transaction processing if resource is sufficient
            if IsResourceSufficient:
                print(f'{MenuItemObjectReturn.name} is {MenuItemObjectReturn.cost}')
                IsMoneyEnough = MoneyMachineVar.make_payment(MenuItemObjectReturn.cost)
                if IsMoneyEnough:
                    CoffeeMakerVar.make_coffee(MenuItemObjectReturn)
                else:
                    loop_on = False

#for gittt
final_function()
