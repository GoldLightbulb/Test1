'''
functions
default arguments
return values

'''

blockchain = [[1]]
name = []


def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])

'''
def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print('-' * 30)
'''

def greet(name):
    print('DJ ' + name)

#greet('Yella')
add_value(10.89)
print('-' * 30)

print(blockchain)