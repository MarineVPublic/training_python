"""Toolkit module."""

def calculate_price(
    unit_price: float,
    quantity: int,
    ) -> float:
    """Calculate the pricing of the given quantity."""
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return unit_price * quantity