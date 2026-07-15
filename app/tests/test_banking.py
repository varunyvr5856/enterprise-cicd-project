from app.banking import BankAccount


def test_deposit():

    account = BankAccount(
        "Varun",
        5000
    )

    result = account.deposit(1000)

    assert result == 6000



def test_withdraw():

    account = BankAccount(
        "Varun",
        5000
    )

    result = account.withdraw(2000)

    assert result == 3000