import Foundation

func powerMod(_ a: Int,_ b: Int,_ c: Int) -> Int{

    guard c > 2 else {return -1}

    if b == 0{
        return 1
    }

    let base = Double(a % c)
    let exponent = Double(b - 1)
    let result = Int(pow(base, exponent)) % c
    return (a % c) * result % c
}

//Test
print(powerMod(2,4,14))