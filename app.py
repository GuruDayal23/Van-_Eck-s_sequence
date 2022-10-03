def main():
    x = int(input("Please enter a number"))
    op = [0,0]
    for _ in range(x):
        lv = op[-1]
        rl = op[:-1][::-1]
        if lv in rl:
            op.append(rl.index(lv)+1)
        else:
            op.append(0)
    print(op)
    
if __name__ == '__main__':
    main()
