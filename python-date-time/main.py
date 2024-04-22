from time import sleep

async def print_and_delay(name):
    print(name)
    await sleep(5)
    print('My Last Name is : Bui')

async def print_first():
    await print('My First Name is: Xuan')

