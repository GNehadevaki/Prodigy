from PIL import Image
import random

def generate_key(image_size, seed):
    random.seed(seed)
    key = list(range(image_size))
    random.shuffle(key)
    return key

def encrypt_image(image_path, output_path, seed, offset):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    key = generate_key(len(pixels), seed)
    
    # Apply mathematical operation and pixel swapping
    encrypted_pixels = [0] * len(pixels)
    for i in range(len(pixels)):
        r, g, b = pixels[i]
        # Apply the mathematical operation (e.g., adding the offset)
        encrypted_r = (r + offset) % 256
        encrypted_g = (g + offset) % 256
        encrypted_b = (b + offset) % 256
        encrypted_pixels[key[i]] = (encrypted_r, encrypted_g, encrypted_b)
    
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, seed, offset):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    key = generate_key(len(pixels), seed)
    
    # Reverse pixel swapping and mathematical operation
    decrypted_pixels = [0] * len(pixels)
    for i in range(len(pixels)):
        r, g, b = pixels[key[i]]
        # Reverse the mathematical operation (e.g., subtracting the offset)
        decrypted_r = (r - offset) % 256
        decrypted_g = (g - offset) % 256
        decrypted_b = (b - offset) % 256
        decrypted_pixels[i] = (decrypted_r, decrypted_g, decrypted_b)
    
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
        if choice == 'q':
            break
        elif choice in ['e', 'd']:
            image_path = input("Enter the path to the image file: ")
            output_path = input("Enter the path for the output image file: ")
            seed = int(input("Enter the seed value: "))
            offset = int(input("Enter the offset value (0-255): "))
            if choice == 'e':
                encrypt_image(image_path, output_path, seed, offset)
            elif choice == 'd':
                decrypt_image(image_path, output_path, seed, offset)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if _name_ == "_main_":
    main()