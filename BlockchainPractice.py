blockchain = [1, 2,]

def add_value():
    blockchain.append([blockchain[0], 5.3])
    print(blockchain)

def add_to_last():
    blockchain.append([blockchain[-1], blockchain[-2]])
    print(blockchain)
    print([blockchain[-1], blockchain[-2]])

# add arguments to f

add_value()
add_to_last()



