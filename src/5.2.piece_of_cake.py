"""
This script calculates the total cost of ingredients needed based on their prices and required quantities.
"""

def piece_of_cake(prices, optionals=None, **kwargs):
    """
    Calculates the total cost of required ingredients, excluding optional ones.

    :param prices: Dictionary of ingredient prices per 100 grams.
    :param optionals: List of ingredient names to exclude from calculation.
    :param kwargs: Quantities of ingredients needed in grams.
    :return: Total cost as an integer.
    """
    total_sum = 0

    for key, value in prices.items():
        if optionals and key in optionals:
            continue

        # Calculate how many grams are needed by dividing by 100
        grams_needed = kwargs.get(key, 0) / 100  # Default to 0 if key not provided
        total_sum += value * grams_needed

    return int(total_sum)

if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
