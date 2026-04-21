import random # This is the "weak" way to make numbers

# 1. HARDCODED PASSWORD
# This is bad because anyone who sees the code knows the password.
password = "admin_password_2026"

# 2. UNUSED VARIABLE
# This is just messy code that takes up memory for no reason.
useless_box = 100

def check_user(username):
    # 3. SQL INJECTION RISK
    # This is bad because a hacker could type "admin' OR 1=1" 
    # and bypass your security.
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    print("Checking database with: " + query)

def make_pin():
    # 4. WEAK RANDOMNESS
    # This is bad because 'random' can be predicted by smart computers.
    return random.randint(1000, 9999)

# Testing the code
check_user("student123")
print("Your PIN is: " + str(make_pin()))
