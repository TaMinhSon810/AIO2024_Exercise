import math

def is_number(n):
    try:
        float(n)
    # Type - casting the string to ‘float ‘.
    # If string is not a valid ‘float ‘ ,
    # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True

# Sigmoid Function
def sigmoid_function(x):
    return 1 / (1 + math.exp(-x))

# ReLU Function
def relu_function(x):
    return 0 if x <= 0 else x

# ELU Function
def elu_function(x):
    alpha = 0.01
    return alpha * (math.exp(x) - 1) if x <= 0 else x

# Calculate activation function
def calc_activation_number(x, act_name):
    if not is_number(x):
        print("x must be a number")
    else:
        x = float(x)
        if act_name == "sigmoid":
            result = sigmoid_function(x)
            print(f"sigmoid: f({x}): {result}")
        elif act_name == "relu":
            result = relu_function(x)
            print(f"relu: f({x}): {result}")
        elif act_name == "elu":
            result = elu_function(x)
            print(f"elu: f({x}): {result}")
        else:
            print(f"{act_name} is not supported")

x = input("Enter a number x: ")
act_name = input("Choose an activation number (sigmoid/relu/elu): ")
calc_activation_number(x, act_name)

