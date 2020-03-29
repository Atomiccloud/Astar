from AStar import AStar
from DisplayGUI import GUI


def main():
    user_input = 0
    while user_input != 'quit':
        user_input = input('Press 1 or 2 to select environment or type quit to exit: ')

        if user_input == '1':
            c_score = int(input('Please input a value for C: '))
            # x max = 30, y max = 18
            start = (1, 14)
            end = (29, 1)

            shape = (((2, 12), (2, 16), (15, 16), (15, 12)),
                     ((1, 5), (2, 9), (6, 10), (8, 5), (5, 1)),
                     ((10, 4), (9, 10), (12, 10)),
                     ((12, 1), (15, 1), (17, 3), (12, 6)),
                     ((19, 1), (24, 1), (24, 9), (19, 9)),
                     ((25, 2), (27, 1), (28, 2), (28, 11)),
                     ((16, 8), (20, 12), (17, 14)),
                     ((22, 12), (25, 10), (27, 12), (27, 15), (24, 16), (22, 15))
                     )
            v = []
            v += shape[0] + shape[1] + shape[2] + shape[3] + shape[4] + shape[5] + shape[6] + shape[7]
            v.append(end)

            edges = ((v[0], v[1]), (v[1], v[2]), (v[2], v[3]), (v[3], v[0]),
                     (v[4], v[5]), (v[5], v[6]), (v[6], v[7]), (v[7], v[8]), (v[8], v[4]),
                     (v[9], v[10]), (v[10], v[11]), (v[11], v[9]),
                     (v[12], v[13]), (v[13], v[14]), (v[14], v[15]), (v[15], v[12]),
                     (v[16], v[17]), (v[17], v[18]), (v[18], v[19]), (v[19], v[16]),
                     (v[20], v[21]), (v[21], v[22]), (v[22], v[23]), (v[23], v[20]),
                     (v[24], v[25]), (v[25], v[26]), (v[26], v[24]),
                     (v[27], v[28]), (v[28], v[29]), (v[29], v[30]), (v[30], v[31]), (v[31], v[32]), (v[32], v[27]))
        elif user_input == '2':
            c_score = int(input('Please input a value for C: '))
            # x max = 30, y max = 18
            start = (2, 5)
            end = (25, 11)

            shape = (((5, 15), (8, 10), (9, 13), (12, 16), (5, 17)),
                     ((3, 3), (11, 1), (10, 7), (4, 8)),
                     ((15, 2), (19, 8), (16, 9), (13, 13)),
                     ((23, 1), (28, 5), (22, 8), (20, 4), (23, 2)),
                     ((17, 11), (24, 10), (26, 17))
                     )
            v = []
            v += shape[0] + shape[1] + shape[2] + shape[3] + shape[4]
            v.append(end)

            edges = ((v[0], v[1]), (v[1], v[2]), (v[2], v[3]), (v[3], v[4]), (v[4], v[0]),
                     (v[5], v[6]), (v[6], v[7]), (v[7], v[8]), (v[8], v[5]),
                     (v[9], v[10]), (v[10], v[11]), (v[11], v[12]), (v[12], v[9]),
                     (v[13], v[14]), (v[14], v[15]), (v[15], v[16]), (v[16], v[17]), (v[17], v[13]),
                     (v[18], v[19]), (v[19], v[20]), (v[20], v[18]))
        elif user_input == 'quit':
            print('Have A Good Day!')
            continue
        else:
            print('Invalid Selection')
            continue

        a = AStar(v, edges, shape, c_score)
        path = a.astar(start, end, user_input)

        if path:
            print(f'path found: {path}')
            GUI(path, v, True, user_input)
        else:
            print('Path not found, Enter higher constraint')


if __name__ == '__main__':
    main()
