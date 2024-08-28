import itertools
import hashlib
from bip44 import Wallet
from mnemonic import Mnemonic

# Constants
MNEMONIC_PHRASE = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"  # Example mnemonic phrase
DERIVATION_PATH = "m/44'/0'/0'/0/0"  # Example derivation path

# Function to calculate a key from a mnemonic and a derivation path
def derive_key_from_mnemonic(mnemonic, derivation_path):
    seed = Mnemonic.to_seed(mnemonic)
    wallet = Wallet(seed)
    key = wallet.derive_account(derivation_path)
    return key

# Function to hash the key
def hash_key(key):
    return hashlib.sha256(key.encode('utf-8')).hexdigest()

# Generate derivation paths (simplified example with limited paths)
def generate_derivation_paths():
    paths = []
    for i in range(10):  # For simplicity, only 10 paths; in real use, this would be exhaustive
        paths.append(f"m/44'/0'/0'/0/{i}")
    return paths

# Main function to try all derivation paths
def brute_force_mnemonic(mnemonic):
    derivation_paths = generate_derivation_paths()
    for path in derivation_paths:
        key = derive_key_from_mnemonic(mnemonic, path)
        key_hash = hash_key(key)
        print(f"Path: {path} - Key: {key} - Hash: {key_hash}")
        # Add your incentivized mechanism here (e.g., reward for finding a specific key)

# Execute
brute_force_mnemonic(MNEMONIC_PHRASE)
