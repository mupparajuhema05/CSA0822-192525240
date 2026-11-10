def otp_check():
    correct = "1234"
    attempts = 0
    while attempts < 3:
        otp = input("Enter OTP: ").strip()
        if not otp:
            print("Blank ignored")
            continue
        if otp == correct:
            print("Access granted")
            return
        attempts += 1
        print("Wrong OTP")
    print("Account locked")
otp_check()
