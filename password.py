import string
import random

def generate_password(length, use_upper, use_lower, use_digits, use_special):
   
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    
    if not characters:
        raise ValueError("At least one character type must be selected")
    
   
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
       
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive number for the length.")
            return
        
       
        use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_lower = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Generated password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
