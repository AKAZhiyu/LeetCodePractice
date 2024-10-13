def main():
    import sys
    input = sys.stdin.read

    data = input().split()

    s_list = list(data[0])
    for i in range(len(s_list)):
        if s_list[i].isdigit():
            s_list[i] = 'number'
    print(''.join(s_list))


if __name__ == "__main__":
    main()
