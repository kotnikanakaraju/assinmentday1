
class ResistorColor:
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }

    tolerance_values = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
        "brown": 1, "red": 2, "gold": 5, "silver": 10
    }

    def decode_resistor_colors(self, *colors):
        if len(colors) == 4:
            value = self.color_values[colors[0]] * 10 + self.color_values[colors[1]]
            multiplier = 10 ** self.color_values[colors[2]]
            tolerance = self.tolerance_values[colors[3]]
        elif len(colors) == 5:
            value = self.color_values[colors[0]] * 100 + self.color_values[colors[1]] * 10 + self.color_values[colors[2]]
            multiplier = 10 ** self.color_values[colors[3]]
            tolerance = self.tolerance_values[colors[4]]
        elif len(colors) == 1:
            value = self.color_values[colors[0]]
            multiplier = 1
            tolerance = 20
        else:
            raise ValueError("Invalid number of color bands")

        ohms = value * multiplier
        units = "ohms"
        if ohms >= 1e6:
            ohms /= 1e6
            units = "megaohms"
        elif ohms >= 1e3:
            ohms /= 1e3
            units = "kiloohms"

        return f"{int(ohms)} {units} ±{tolerance}%"

if __name__=="__main__":
    resistor_color = ResistorColor()
    print(resistor_color.decode_resistor_colors("orange", "orange", "black", "green"))
    print(resistor_color.decode_resistor_colors("orange", "orange", "orange", "grey"))
    print(resistor_color.decode_resistor_colors("orange", "orange", "blue", "red"))
