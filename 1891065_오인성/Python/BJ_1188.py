sausage, critic= map(int, input().split())

def Sausage_cut(S, C) :
    if S % C == 0 :
        return C
    return Sausage_cut(C, S%C)

print(critic-Sausage_cut(sausage,critic))

asdasdasd