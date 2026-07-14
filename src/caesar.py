def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

def main():

    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'ENCRYPT', 'D', 'DECRYPT']:
        print("Invalid choice. Please enter E or D.")
        return

    text = input("Enter your text: ")

    try:
        shift = int(input("Enter the shift key (1-25): "))
    except ValueError:
        print("Error: The shift key must be a whole number.")
        return

    if choice in ['E', 'ENCRYPT']:
        result = encrypt(text, shift)
        print(f"\nEncrypted text: {result}")
    else:
        result = decrypt(text, shift)
        print(f"\nDecrypted text: {result}")

if __name__ == "__main__":
    main()
