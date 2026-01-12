def add_matrices():
    try:
        n = int(input("Введите размер матрицы: "))
        if n <= 2:
            print("Error!")
            return
        
        print("Введите первую матрицу:")
        matrix1 = [list(map(int, input().split())) for _ in range(n)]
        
        print("Введите вторую матрицу:")
        matrix2 = [list(map(int, input().split())) for _ in range(n)]
        
        print("Результат:")
        for i in range(n):
            print(' '.join(str(matrix1[i][j] + matrix2[i][j]) for j in range(n)))
            
    except:
        print("Error!")

add_matrices()