from pathlib import Path
from Crypto.PublicKey import RSA

# Define paths for our key files
PROJECT_FOLDER = Path(__file__).parent.parent
PRIVATE_KEY_FILE = PROJECT_FOLDER / "my_keypair"  # Contains the private key
PUBLIC_KEY_FILE = PROJECT_FOLDER / "my_keypair.pub"  # Contains the public key

# Make sure our key files exist before proceeding
assert Path.exists(PRIVATE_KEY_FILE)
assert Path.exists(PUBLIC_KEY_FILE)

# Load the private key from file
# The private key must be kept secret and secure
with open(PRIVATE_KEY_FILE, "r", encoding="utf8") as key_file:
    private_key = RSA.import_key(key_file.read())

# Extract the public key from our private key
# The public key can be freely shared with anyone
public_key = private_key.publickey()
print(f"Public key:\n{public_key.export_key().decode('utf-8')}")