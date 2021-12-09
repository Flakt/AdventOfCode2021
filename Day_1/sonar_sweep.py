from os import name


def depth_times():
    current_depth = 0
    depth_increases = 0
    with open('./depths.txt', 'r') as f:
        depths = list(map(int,f.readlines()))
        for depth in depths:
            if current_depth < depth:
                depth_increases+=1
            current_depth = depth
    print(depth_increases - 1)


def depth_three_sums():
    current_sum = 0
    sum_increases = 0
    with open('./depths.txt', 'r') as f:
        depths = list(map(int, f.readlines()))
        for index in range(len(depths) - 2):
            depth_sum = depths[index] + depths[index + 1] + depths[index + 2]
            if current_sum < depth_sum:
                sum_increases+=1
            current_sum = depth_sum
    print(sum_increases - 1)



if __name__ == '__main__':
    depth_times()
    depth_three_sums()