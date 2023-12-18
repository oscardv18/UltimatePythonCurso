class MiError(Exception):
    """Error custom class
    Args:
        Exception (error): Crea un error personalizado para las divisiones por 0
    """
    def __init__(self, message, codex):
        self.message = message
        self.codex = codex
    
    def __str__(self):
        return f"{self.message} - codigo: {self.codex}"

def div(n = 0):
    """div function
    Args:
        n (int, optional): division function. Defaults to 0.
    Raises:
        MiError: Se lanza cuando ocurre una division entre 0
    Returns:
        int: division result
    """
    if n == 0:
        raise MiError("No se puede dividir entre 0", 3312)
    return 5 / n

try:
    div()
except MiError as e:
    print(e)
