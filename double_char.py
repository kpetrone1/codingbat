def double_char(str):
    """
    Given a string, return a string where for every 
    char in the original, there are two chars.
        """
    double_char = ''
    for char in str:
        double_char += char *2
    return double_char

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'