# FOR loops, used to loop thru elements in a list
# WHILE loops, executes as long as a condition is true (make sure to provide exit condition)


# BREAK ends the loop
# continue only skips the rest of the code but restarts the loop from fresh


# IS
# IN

#


# this is a global variable that can be used everywhere
blockchain = []


def get_last_blockchain_value():
    # add an additional check whether the value exists or not
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction = [1]):
    # if equals none, a different last_transaction will be appended
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input =  float(input('your transaction amount please:'))
    return user_input


def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('outputing block...')
        print(block)
    else:
        print('-' * 25)

def verify_chain():
    block_index = 0
    is_Valid = True
    # remember when it comes to the range() function it only excludes the number you put in
    # ex: range(5) = 0, 1, 2, 3, 4 
    # in this case the following will go all the way up the the length of blockchain - 1
    # good alternative to the basic for cases, partly interested in elements of list, but more interested in indexes of a list
    # to start at a different place do this --> for i in range(5,10) = 5, 6, 7, 8, 9
    # hell or even this way which increments by 2 ---> range(5, 20, 2) = 5, 7, 9, 11, 13, 15, 17, 19
    # doesnt work because it can't work with float ---> range(5.0, 10.0, 0.5) = 
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue

        # compares the first value of the currently outputed block chain to the last block chain outputed
        # block[0] = first element of second block
        # blockchain[block_index - 1] = entire previous block or the previously updated blockchain list

        # blockchain and block_index are both lists within one another
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_Valid = True
        else:
            is_Valid = False
            break
        block_index += 1
    return is_Valid
    


waiting_for_input = True

# constantly queries for input until exit condition is provided
while waiting_for_input:
    print('please choose')
    print('1. Add a new transaction value')
    print('2. output the block chain blocks')
    print('h: manipulate the chain')
    print('Q: To Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        ts_amount = get_transaction_value()
        add_transaction(ts_amount, get_last_blockchain_value())
    elif user_choice == '2': 
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        # alternative to breaking
        waiting_for_input = False
    else:
        print("invaild input, type in a number between 1 and 2")
    if not verify_chain():
        print('Invalid blockchain!')
        break
# else case executes when loop is done
else: 
    print('user left')

#print('Done!')

