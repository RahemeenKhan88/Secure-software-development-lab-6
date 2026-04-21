import os       # Required for Fix 1
import secrets  # Required for Fix 3

# FIX 1: Removed hardcoded password. 
# Now it looks for a system variable instead of writing it in the code.
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# FIX 4: Removed the 'useless_box' variable entirely.

def check_user(username):
    # FIX 2: Prepared Statements (Conceptual)
    # To fix SQL injection, we never use + to add strings.
    # In a real database, we would use a '?' placeholder.
    print("Checking database securely for user...")
    # Example: cursor.execute("SELECT * FROM users WHERE name = ?", (username,))

def make_pin():
    # FIX 3: Using 'secrets' instead of 'random'
    # This is cryptographically secure and much harder to guess.
    return secrets.randbelow(9000) + 1000

# Testing the secure code
check_user("student123")
print("Your Secure PIN is: " + str(make_pin()))
