from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Load the image
    image = Image.open(input_image_path)
    pixels = np.array(image)

    # Encrypt the pixels using XOR
    encrypted_pixels = pixels ^ key

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    # Load the encrypted image
    encrypted_image = Image.open(input_image_path)
    encrypted_pixels = np.array(encrypted_image)

    # Decrypt the pixels using XOR
    decrypted_pixels = encrypted_pixels ^ key

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_image_path)

# Example usage
key = 123  # Example key (should be more complex in practice)
encrypt_image('original_image.png', 'encrypted_image.png', key)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key)