def build_matrix(rows, cols):
    matrix = []
    column_list = []

    for cols in (range(cols)):
        column_list.append(0)
    
    for rows in (range(rows)):
        matrix.append(column_list)

    return matrix