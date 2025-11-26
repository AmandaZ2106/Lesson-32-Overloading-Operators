class RomanConverter:
    def to_roman(self, num):
        roman_dict = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1}
        

        result = ""

        for symbol, value in roman_dict.items():
            while num >= value:
                result += symbol
                num -= value

        return result

n = int(input("Enter a number: "))
converter = RomanConverter()
print("Roman numeral:", converter.to_roman(n))
