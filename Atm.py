class atm():
    def __init__(self, atmCardNo, pinNo):
        self.atmCardNo = atmCardNo
        self.pinNo = pinNo

    def cashWithdrawal(self):
        print("Withdrew cash successfully")

    def balanceEnquiry(self):
        print("Balance Enquiry Successful")

bank = atm("12546325658", "1111")
print(bank.balanceEnquiry())
print(bank.cashWithdrawal())