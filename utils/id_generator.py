class IDGenerator:
    """Generates business IDs for the ERP simulator."""

    @staticmethod
    def generate(prefix: str, number: int, digits: int = 5) -> str:
        """
        Generate a formatted business ID.

        Example:
        SUP00001
        PROD00125
        CUST10542
        """
        return f"{prefix}{number:0{digits}d}"
    
    