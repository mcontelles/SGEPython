def esSudokuCorrecto(miSudoku):
    for fila in miSudoku:
        if len(set(fila)) != 9 or sum(fila) != 45:
            return False
    
    for col in range(9):
        columna = [miSudoku[fila][col] for fila in range(9)]
        if len(set(columna)) != 9 or sum(columna) != 45:
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [miSudoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subgrid)) != 9 or sum(subgrid) != 45:
                return False
    
    return True

sudoku_correcto = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

resultado = esSudokuCorrecto(sudoku_correcto)
print(resultado)
