class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (75, 212, 59)
    DARK_GREEN = (10, 100, 16)
    BLUE = (48, 72, 159)
    DARK_BLUE = (31, 23, 234)
    YELLOW = (235, 150, 34)
    BEIGE = (239, 220, 185)
    DARK_BEIGE = (219, 190, 135)
    ORANGE = (239, 132, 74)
    DARK_ORANGE = (219, 102, 24)

    def lerp(color1: 'tuple[int, int, int]', color2: 'tuple[int, int, int]', t: float) -> 'tuple[int, int, int]':
        r = color1[0] + ((color2[0] - color1[0]) * t);
        g = color1[1] + ((color2[1] - color1[1]) * t);
        b = color1[2] + ((color2[2] - color1[2]) * t);
        return (r, g, b)