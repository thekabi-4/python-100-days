def convert_currency(amount: float, from_currency: str, to_currency: str, rates: dict) -> float:
    # Same currency case
    if from_currency == to_currency:
        return round(amount, 2)
    
    # Check if both currencies exist in rates
    if from_currency not in rates or to_currency not in rates:
        return -1.0
    
    # Perform conversion
    converted = amount * rates[from_currency] / rates[to_currency]
    return round(converted, 2)


# Example test
rates = {"USD": 1.0, "EUR": 0.85}
result = convert_currency(100, "USD", "EUR", rates)
print(result)   # Expected: 117.65