def calc_submarine_part_1():
    horizontal = 0
    vertical = 0
    with open('./commands.txt', 'r') as f:
        commands = [com.strip() for com in f]
        for line in commands:
            command = line.split()
            if command[0] == 'forward':
                horizontal = horizontal + int(command[1])
            elif command[0] == 'down':
                vertical = vertical + int(command[1])
            elif command[0] == 'up':
                vertical = vertical - int(command[1])
        print(horizontal * vertical)


def calc_submarine_part_2():
    horizontal = 0
    vertical = 0
    aim = 0
    with open('./commands.txt', 'r') as f:
        commands = [com.strip() for com in f]
        for line in commands:
            command = line.split()
            if command[0] == 'forward':
                horizontal = horizontal + int(command[1])
                vertical = vertical + (aim * int(command[1]))
            elif command[0] == 'down':
                aim = aim + int(command[1])
            elif command[0] == 'up':
                aim = aim - int(command[1])
    print(horizontal * vertical)


        
        

if __name__ == '__main__':
    calc_submarine_part_1()
    calc_submarine_part_2()