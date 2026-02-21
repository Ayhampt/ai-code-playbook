def alphabeta(depth,index,alpha,beta,isMax,values):
    indent = " " * depth
    if depth == 2:
        print(f"{indent}Leaf -> {values[index]}")
        return values[index]
    if isMax:
        best = -1000
        print(f"{indent}MAX node")
        for i in range(2):
            val = alphabeta(depth+1,index*2+i,alpha,beta,False,values)
            best = max(best,val)
            alpha = max(alpha,best)

            if beta <= alpha:
                print(f"{indent}PRUNED")
                break
        print(f"{indent}MAX returns {best}")
        return best
    else:
        best = 1000
        print(f"{indent}MIN node")
        for i in range(2):
            val = alphabeta(depth+1,index*2+i,alpha,beta,True,values)
            best = min(best,val)
            beta = min(beta,best)

            if beta <= alpha:
                print(f"{indent}PRUNED")
                break
        print(f"{indent}MIN returns {best}")
        return  best
values = [3,5,2,9]
print("\nFinal Optimal Value:",alphabeta(0,0,-1000,1000,True,values))


