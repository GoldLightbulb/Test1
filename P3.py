# Tuples
# sets
# dictionaries

# all of these are iterable
# you can also do list comprehension

# difference between By reference(is), and By value(==)

# send transactions from A to B

# transaction mining

# (pass means don't do anything in the functions)

# lets first understanding the data structure we need for this

# transactions need a sender, reciepent and amount (this occurs multiple times, and are each time used to mine a block for coins and such)

# lets start by adding something that helps with managing outstanding transactions, adding a new block, and making sure we add a transaction for that

# need a data structure that adds key value pairs and for outstanding transactions

# iterable (loop through them) lists [] (ordered lists with duplicated), sets {} (unordered with no duplicates)

# and Tuples {) (noneditable, ordered, and duplicates are allowed) --> useful for hardcoded defaults

# and dictionary {} (editable, unoreded, no duplicates, like a map)

# list comprehensions --> alternative of for loops, ex: d_l = [el * 2 for el in simple list] we tell python what we want to do with each element in a called list 
# in this ex: im multiplying every element from tge simple list by 2 and storing it into d_l

# now lets combine list comprehensions with "if"
# Ex: simple_list = [1, 2, 3, 4]
      # duplicate an element in a list by 2 for every element in the simple list IF the element is divisible by 2
#     dup_list = [el * 2 for el in simple_list if el % 2 == 0]
#     this will output as [4,8]

      # duplicate an element in a list by 2 for every element in the simple list IF the element is in the calc_items list
#                [el * 2 for el in simple_list if el in calc_items]
#



# dict comprehensions --> Ex: stats = [('age', 29), ('weight', 72), ('height', 178)]
#                         dict_stats = {key: value for (key, value) in stats}
# the tuples here are converted into dictionary values after outputing dict_stats

# normal lists should work for the transactions

    # blocks should be dictionaries, with hash keys
    # previous_hash means the summarized value of the block prior to this block in the blockchain
    # by lening block chain you keep it untaken

import time

# global constant variable remains unchanged
MINING_REWARD = 10

genesis_block = {'previous_hash': '', 
                'index' : 0, 
                'transactions' : [] 
                }
# this is the genesis block, a value needed to be stored at the beginning of the block chain
blockchain = [genesis_block]
open_transactions = []
owner = 'Mota'
# set is a data structure
participants = {'Adam'}

# to verify, we need this function to hash a block, mine one, and most importantly verify it 
# note, this is done with ANY block not just the last one as earlier
def hash_block(block): 
    return '-'.join([str(block[keys]) for keys in block])

# get balance of ANY participant (why it's passed through)
def get_balance(participant):
    # interested in transactions where the particpant is the center, so use a nested list comphrension
    # transactions['amount'] for transactions in a block, while storing the transaction amount in a list


    # nested list comprehensions
    # get the amount for the given transaction for all transactions in a block
    # if the transaction sender is equal to the participant
    # all while going thru each block in the blockchain
    # this is also very important for mining a block 
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # also consider the amount sent to the open_transactions 
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        # if the transaction list has one element (otherwise it will get an error)
        if len(tx) > 0:
        # accesses first element in transaction
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        # if the transaction list has one element (otherwise it will get an error)
        if len(tx) > 0:
        # accesses first element in transaction
            amount_recieved += tx[0]
    # amount_recieved minus the amount_sent is the total current balance
    # when you send the very first transaction upon running the program and mine it, you'll get a negative balance
    return amount_recieved - amount_sent 


def get_last_blockchain_value():
    # add an additional check whether the value exists or not
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    # transactions must include the sender so include them in along with their balance for verification
    sender_balance = get_balance(transaction['sender'])
    # if the sender can't afford the amount they're trying to send then return true
    # this is the same way to write a concise if statement with a return true or false, because it automatically will return either true of false to the user
    return sender_balance >= transaction['amount']

# the following function accepts two arguments
# 1. (transaction amount)
# 2. an optional (last_transaction amount) (optional b/c it has the default value of [1])
# now that you're creating blockchains, you're no longer interested in comparing the current transaction with the last one
# you are now storing a new transaction (like the sender, reciepent and amount)
def add_transaction(recipient, sender = owner, amount = 1.0):
    # the sender of the coins
    # recipient of the coins
    # amount of coins sent with the transaction (default = 1.0)
    # dictionary
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount' : amount
        }
    
    # invalid transactions make it into the open transactions list
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        # return true when transaction has been verified
        return True
    # return false when it has failed
    return False
    
# creates new block for the blockchain (processing the transactions)
# the idea here is that when this function gets called, all open transactions are taken and are added to a new block and to the blockchain
# this is how the blockchain works

# we are adding the reward system to the mine_block function to let the user know that they have successfully mined it
# this true in the real world since blockchains are very hard and long to mine
def mine_block():
    # initially, indexing the block at the very first block will be empty (so an error), any blockchain needs to have a genesis block to prevent error
    last_block = blockchain[-1]
    
    hashed_block = hash_block(last_block)
    reward_transaction = {
                        'sender': 'MINING', 
                        'recipient': owner, 
                        'amount' : MINING_REWARD
                        }
    # we are adding this variable as a means to properly distribute the reward to a user if their transaction were to be successful
    # don't be tempeted to set copied transactions equal to open transactions(without ranging it), b/c lists just like the other important complex data structures
    # (everything but booleans numbers and strings) are copied by 'reference' and not value
    copied_transactions = open_transactions[:]
    #append the reward transactions to the open_transactions list
    open_transactions.append(reward_transaction)

    # good example of list comprehension, interested in value so --> (last_block(keys))
    # join calls the list as an argument which will be joined by the given character (only works in a list of strings)
    # concatinate it all with one long string
    #for keys in last_block:
        #value = last_block[keys]
        #hashed_block = hashed_block + str(value)

    # make sure to reset the participant's transactions
    #print(hashed_block)
    block = {'previous_hash': hashed_block, 
             'index' : len(blockchain), 
             'transactions' : open_transactions }
    
    blockchain.append(block)
    # local variable so it doesn't use the global one and get an error
    # eventually because you're mining a block, you need the function the rest the transactions
    return True

def get_transaction_value():
    tx_recipient = input('Enter the sender of the transaction : ')
    tx_amount =  float(input('your transaction amount please : '))
    # this is a tuple, if you had one value on the other hand, type this in (tx_recipient, )
    # empty tuple ()  but its useless
    return (tx_recipient, tx_amount)

def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('outputing block...')
        print('\n',block)
    else:
        print('-' * 25)

# based on our current code, this logic won't work any more so lets start from scratch
#def verify_chain():
#    block_index = 0
#    is_Valid = True
#    for block_index in range(len(blockchain)):
#        if block_index == 0:
#            block_index += 1
#            continue
#        elif blockchain[block_index][0] == blockchain[block_index - 1]:
#            is_Valid = True
#        else:
#            is_Valid = False
#            break
#        block_index += 1
#    return is_Valid



# lets verify our blocks in a new way
# we need to hash our old block and storing the hashed version of a block in a field(key) of the next block
# this is how we will verify our blocks
# if the value of the previos hash we store in a block doesn't match the recaculated hash, this means there has
# been a change in the previous block in the meantime, and is therefore invalid
def verify_chain():
    # verify the current blockchain and return True if its valid, False otherwise
    # loop thru all the blocks in the blockchain do do the comparisons for each block
    # if you wrap a list in the enumerate function it will give back a tuple with two pieces of Info, 
    # the index of the element and the element itself
    for (index, block) in enumerate(blockchain):
        # get index of blockchain that way so you can skip that for the very first block (genesis block)
        # this condition is to ignore the validation of the genesis block
        if index == 0:
            continue
        # compare the previous hash key to the last block of the blockchain (remember to hash the last block since you're calling it in a hashed argument, using the hashed_block fn)
        # you're dynamically recalculating the value of the last block and comparing it to the previously hased block
        # if it doesn't compare
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True
    

def verify_transactions():
    # verify transaction returns true for "all" transaction in open transactions
    return all([verify_transaction(tx) for tx in open_transactions])

    #is_Valid = True
    #for tx in open_transactions:
        #if verify_transaction(tx):
            #is_Valid = True
        #else:
            #is_Valid = False
    #return is_Valid

waiting_for_input = True

# constantly queries for input until exit condition is provided
while waiting_for_input:
    print('please choose')
    print('1. Add a new transaction value')
    print('2. Mine a new block')
    print('3. output the block chain blocks')
    print('4. output participants')
    print('5. Check Transaction validity')
    print('h. manipulate the chain')
    print('Q. To Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # tuple unpacking, into new variables 
        # pulls out the first element of the tuple and stores it in the first variable, and the second element to the second variable
        recipient, amount = tx_data
        # add transaction amount to blockchain (lets add a tuple here)
        # allows to skip optional sender argument which is already populated by the hardcoded default owner
        # hence the reason why you don't see a sender argument here, or you can omit it and use it without it
        if add_transaction(recipient, amount = amount):
            print('Adding transaction...')
            time.sleep(2)
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2': 
        if mine_block():
            # reset the participant's number of coins
            open_transactions = []
    elif user_choice == '3': 
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5': 
        if verify_transactions():
            print('All Transactions are valid')
        else: 
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            # hack genesis block?
            blockchain[0] = {'previous_hash': '', 
                            'index' : 0, 
                            'transactions' : [{'sender': 'Chris', 'recipient': 'Max', 'amount' : 100.0}] 
                            }
    elif user_choice == "q":
        # alternative to breaking
        waiting_for_input = False
    else:
        print("invaild input, type in a number between 1 and 2")
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
    print(get_balance('Mota'))
# else case executes when loop is done
else: 
    print('user left')

print('Done!')





