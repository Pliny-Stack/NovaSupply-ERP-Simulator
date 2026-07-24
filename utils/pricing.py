class PricingEngine:
    """Business pricing calculations."""

    @staticmethod
    def calculate_price(cost: float, margin: float) -> float:
        """
        Calculate selling price.

        Formula:
        Selling Price = Cost × (1 + Margin)
        """

        return round(cost * (1 + margin), 2)