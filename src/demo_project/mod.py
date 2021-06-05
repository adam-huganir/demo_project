class ADemoClass:
    """Which has a docstring"""

    def __init__(self):
        """
        and an init docstring

        >>> adc = ADemoClass()
        >>> adc.add(4)
        8

        """

    def add(self, num: int):
        return num + num
