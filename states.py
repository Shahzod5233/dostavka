from aiogram.dispatcher.filters.state import State,StatesGroup

# Procesi dlya regestratsii
class Registration(stateGroup):
    getting_name_state =  State()
    getting_phone_number = State()
    getting_lokation =State()
    getting_gender = State()

# Procesi dlya Vibora opredelyonnogo tovora
class GetProduct(StatesGroup):
    getting_pr_name =State()
    getting_pr_count = State()

# Procesi pri rabote s korzinoy
class Cart(StatesGroup):
    waiting_for_product = State()
    waiting_new_count = State()


# Procesi pri oformlenii zakaza
class Order(StatesGroup):
    waiting_location = State()
    waiting_pay_type = State()
    waiting_accapt = State()