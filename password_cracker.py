import hashlib

def hash_password(password: str, algorithm: str = 'sha256') -> str:
    """
    Hash a password using the specified algorithm.
    Supported algorithms: 'md5', 'sha256', 'sha1'
    """
    password_bytes = password.encode('utf-8')
    
    if algorithm == 'md5':
        return hashlib.md5(password_bytes).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password_bytes).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password_bytes).hexdigest()
    else:
        raise ValueError("Unsupported algorithm. Choose between 'md5', 'sha1', or 'sha256'.")

# Test the function
if __name__ == "__main__":
    # Print the hash of a sample password
    print(hash_password("Atlas", "sha256"))
