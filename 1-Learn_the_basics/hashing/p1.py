def hash(n: int,nums: list[int]):
    hash_dict ={}
    for n in nums:
        if n in list(hash_dict.keys()):
            hash_dict[n] += 1
            continue
        hash_dict[n] = 1
    return hash_dict
    

def main(n: int,nums: list[int],f_nums: list[int]):
    hash_dict = hash(n,nums)
    for i in f_nums:
        print(hash_dict[i])


if __name__ == '__main__':
    main(5,[5,9,5,6,3],[5,9,3])