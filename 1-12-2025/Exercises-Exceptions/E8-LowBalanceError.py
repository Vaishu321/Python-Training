class LowBalanceError(Exception):
    pass

def withdraw(Amount, Balance):
    if Amount > Balance:
        raise LowBalanceError
    return Amount - Balance

withdraw(110,100)
