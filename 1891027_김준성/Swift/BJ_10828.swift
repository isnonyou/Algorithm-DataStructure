import Foundation

var order = [String]()
var stack = [Int]()
var num = Int(readLine()!)!

for _ in 0..<num {
    order.append(readLine()!)
}

for o in order {
    let temp = o.split(separator: " ")
    switch(temp[0]) {
    case "push":
        stack.append(Int(temp[1])!)
    case "pop":
        if stack.isEmpty {
            print(-1)
        }
        else {
            let l = stack.endIndex - 1
            print("\(stack[l])")
            stack.remove(at: l)
        }
    case "size":
        print(stack.count)
    case "empty":
        if stack.isEmpty {
            print(1)
        }
        else {
            print(0)
        }
    default:
        if stack.isEmpty {
            print(-1)
        }
        else {
            print(stack[stack.endIndex - 1])
        }
    }
}