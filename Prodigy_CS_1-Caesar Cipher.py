def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
        if choice == 'q':
            break
        elif choice in ['e', 'd']:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                result = encrypt(text, shift)
                print("Encrypted text:", result)
            elif choice == 'd':
                result = decrypt(text, shift)
                print("Decrypted text:", result)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if _name_ == "_main_":
    main()