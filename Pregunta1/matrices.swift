func magicSquare(_ matrix: [[Int]]) -> Bool {
    let n = matrix.count
    guard n > 0 else {return false}
    
    //Calculate the sum of the first row and thats the expected value
    var expectedSum = 0
    for i in 0..<n{
        expectedSum += matrix[0][i]
    }
    
    //Check rows and columns, loop 0
    for i in 0..<n{
        //Variables
        var rowSum = 0
        var columnSum = 0
        //loop 1
        for j in 0..<n{
            rowSum += matrix[i][j]
            columnSum += matrix[j][i]
        }
        //Check the sum if equal to de expected
        if rowSum != expectedSum || columnSum != expectedSum {
            return false
        }
    }
    
    //Check diagonal
    var mainDiagonalSum = 0
    var otherDiagonalSum = 0
    for i in 0..<n{
        mainDiagonalSum += matrix[i][i]
        otherDiagonalSum += matrix[i][n - i - 1]
    }
    
    return mainDiagonalSum == expectedSum && otherDiagonalSum == expectedSum
}

//Test
let matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if magicSquare(matrix) {
    print("The matrix is a Magic square.")
} else {
    print("The matrix is not a Magic square.")
}
