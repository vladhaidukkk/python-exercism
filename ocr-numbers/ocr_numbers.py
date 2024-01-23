W, H = 3, 4
SYMBOLS = {
    (
        " _ ",
        "| |",
        "|_|",
        "   ",
    ): "0",
    (
        "   ",
        "  |",
        "  |",
        "   ",
    ): "1",
    (
        " _ ",
        " _|",
        "|_ ",
        "   ",
    ): "2",
    (
        " _ ",
        " _|",
        " _|",
        "   ",
    ): "3",
    (
        "   ",
        "|_|",
        "  |",
        "   ",
    ): "4",
    (
        " _ ",
        "|_ ",
        " _|",
        "   ",
    ): "5",
    (
        " _ ",
        "|_ ",
        "|_|",
        "   ",
    ): "6",
    (
        " _ ",
        "  |",
        "  |",
        "   ",
    ): "7",
    (
        " _ ",
        "|_|",
        "|_|",
        "   ",
    ): "8",
    (
        " _ ",
        "|_|",
        " _|",
        "   ",
    ): "9",
}


def convert(input_grid):
    if len(input_grid) % H != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % W != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    groups = []
    for i in range(0, len(input_grid), H):
        groups.append([])
        for j in range(i, i + H):
            row = input_grid[j]
            for k in range(0, len(row), W):
                col = row[k : k + W]
                if j % H == 0:
                    groups[-1].append([col])
                else:
                    groups[-1][k // W].append(col)

    symbols = []
    for i, group in enumerate(groups):
        for symbol in group:
            symbols.append(SYMBOLS.get(tuple(symbol), "?"))
        if i != len(groups) - 1:
            symbols.append(",")
    return "".join(symbols)
