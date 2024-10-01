"""
test docstring


"""


def add_numbers(a: int, b: int) -> int:
    return a + b


def greet_user(name: str) -> int:
    print(f"Hello, {name}!")
    return name  # Ceci est une erreur car "name" est de type str, mais la fonction attend un int


def process_data(data: list[int]) -> str:
    if len(data) > 0:
        return data[0]  # Erreur : retourne un int mais devrait retourner un str
    return "No data"
