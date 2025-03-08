import random
import string

def generate_password(
    length: int = 12, 
    uppercase: bool = False, 
    lowercase: bool = False, 
    digits: bool = False, 
    specialChars: bool = False
) -> str:
    
    """Generate a password 

        Parameters
        ----------

        length : int or None
            Desired length of the password.

        uppercase : bool or None
            Whether to include the Uppcase Letters or not.

        lowercase : bool or None
            Whether to include the Uppcase Letters or not.

        digits : bool or None
            Whether to include the Uppcase Letters or not.

        specialChars : bool or None
            Whether to include the Uppcase Letters or not.                
        """

    
    charactors = ''

    if uppercase:
        charactors += string.ascii_uppercase
    
    if lowercase:
        charactors += string.ascii_lowercase
    
    if digits:
        charactors += string.digits

    if specialChars:
        charactors += string.punctuation


    return ''.join(random.choice(charactors) for _ in range(length))
