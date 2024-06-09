import numpy as np

def calculate_one_loss_function(y_true, y_pred, loss_name):
    if loss_name == "MAE":
        return np.abs(y_true - y_pred)
    else:
        return np.square(y_true - y_pred)
    
def calculate_loss_function(total_loss, loss_name, n):
    if loss_name == "RMSE":
        return np.sqrt(total_loss/n)
    else:
        return total_loss/n
    
def regression_loss_function():
    n = input("Input number of samples (integer number) which are generated: ")
    if not n.isnumeric():
        print("Number of sample sizes must be an integer number")
    else:
        loss_name = input("Choose a loss function (MAE/MSE/RMSE): ")
        n = int(n)
        total_loss = 0
        for i in range(n):
            predict = np.random.uniform(0, 10)
            target = np.random.uniform(0, 10)

            loss = calculate_one_loss_function(target, predict, loss_name)

            total_loss += loss

            print(f"Loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")

    final_loss = calculate_loss_function(total_loss, loss_name, n)

    print(f"final {loss_name}: {final_loss}")

regression_loss_function()