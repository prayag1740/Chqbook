class Config:
    
    class GENERIC:
        SUCCESS                 = (0, "Success")
        FAILURE                 = (2, "Some issue occured. Please try again later")    
    
    
    class MISSING:
        AMOUNT                  = (1, "Please enter amount to continue")
        PAYMENT_ID              = (2, "Payment ID is missing")
        AMOUNT                  = (3, "Amount is missing")
        
    class PAYMENT:
        INVALID_AMT              = (1, "Please enter a valid amount to continue")
        INVALID_PAYMENT          = (2, "Invalid Payment ID")
        