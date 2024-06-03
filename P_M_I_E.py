from PIL import Image

def encrypt_image(image_path, key, mode='encrypt'):
  """
  Encrypts or decrypts an image using pixel manipulation (XOR with key).

  Args:
      image_path: Path to the image file.
      key: A single integer value as the encryption key.
      mode: 'encrypt' for encryption, 'decrypt' for decryption (default: 'encrypt')
  """
  # Open image
  image = Image.open(image_path).convert('RGB')
  width, height = image.size

  # Get image data as pixels
  pixels = image.load()

  # Encrypt or decrypt each pixel
  for i in range(width):
    for j in range(height):
      r, g, b = pixels[i, j]
      if mode == 'encrypt':
        new_r = (r ^ key) % 256
        new_g = (g ^ key) % 256
        new_b = (b ^ key) % 256
      else:
        new_r = (r ^ key) % 256
        new_g = (g ^ key) % 256
        new_b = (b ^ key) % 256
      pixels[i, j] = (new_r, new_g, new_b)

  # Save the encrypted/decrypted image
  if mode == 'encrypt':
    new_path = f"{image_path.split('.')[0]}_encrypted.png"
  else:
    new_path = f"{image_path.split('.')[0]}_decrypted.png"
  image.save(new_path)

# Get user input
image_path = input("Enter the image path: ")
key = int(input("Enter the encryption key (integer): "))
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

# Check for valid mode
if mode not in ('encrypt', 'decrypt'):
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

# Encrypt or decrypt the image
encrypt_image(image_path, key, mode)

print(f"{mode.capitalize()}d image saved!")