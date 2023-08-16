def get_puzzle(puzzle_number):
    given_letters, encoded, solution = list(puzzles[puzzle_number].values())
    
    code_dict = {i:"." for i in range(1, 27)}
    for num, letter in given_letters.items():
        code_dict[num] = letter
        
    return code_dict, encoded, solution


puzzles = {12: {'given_letters': {4: 's', 20: 'r', 23: 'i'},
                'encoded_words': [[4, 2, 25, 25, 15, 25],
                                    [24, 12, 20, 26, 20, 1, 8],
                                    [10, 2, 14, 23, 26],
                                    [3, 1, 23, 20, 4, 24, 20, 1, 8],
                                    [2, 23, 25, 18, 25],
                                    [23, 21, 23, 12, 26, 23, 18],
                                    [1, 18, 25],
                                    [25, 11, 12, 2, 8],
                                    [1, 2, 8],
                                    [1, 2, 17, 23, 25, 26, 8],
                                    [2, 25, 23, 7, 3],
                                    [9, 12, 18, 19, 4, 5, 23, 26, 3],
                                    [4, 25, 17, 26, 1, 2, 26],
                                    [20, 25, 5, 25, 21, 8],
                                    [4, 13, 10, 23, 2, 26],
                                    [25, 2, 14, 25, 25, 11, 9, 25],
                                    [15, 23, 26, 3, 25, 20],
                                    [6, 12, 8, 20, 23, 21, 23, 2, 7],
                                    [4, 26, 25, 24, 4, 12, 2],
                                    [26, 1, 17, 1, 26, 23, 12, 2],
                                    [18, 12, 2, 21, 12, 2, 25, 21],
                                    [20, 23, 18, 19, 25, 26, 8],
                                    [1, 11, 1, 26, 25, 5, 25, 2, 26],
                                    [23, 2, 3, 1, 9, 25],
                                    [1, 18, 26, 23, 16, 1, 26, 25],
                                    [22, 3, 25, 25, 15, 8]],
                'solution': dict(zip(range(1, 27), "anhsmjgyluboqfzvxckrdwipet"))},
           
           13: {'given_letters': {4: 's', 19: 'u', 25: 'n'},
                'encoded_words': [[11, 24, 7, 8, 24, 17],
                                     [23, 19, 13, 14, 24, 7],
                                     [4, 16, 13, 5, 3, 1, 25, 16],
                                     [10, 22, 10, 16],
                                     [26, 23, 1, 19, 9],
                                     [4, 3, 1, 19, 9, 24, 17],
                                     [17, 6, 4, 14, 10, 25, 17, 24, 17],
                                     [6, 25, 4, 19, 23, 6, 25],
                                     [25, 16, 23, 1, 25],
                                     [17, 6, 7, 9],
                                     [10, 5, 5, 7, 1, 12, 10, 23],
                                     [26, 19, 9, 19, 7, 24],
                                     [22, 3, 24, 24, 20, 24],
                                     [7, 24, 21, 16, 21, 23, 24],
                                     [4, 8, 6, 5],
                                     [6, 17, 6, 1, 13],
                                     [5, 23, 10, 16, 9, 3, 6, 25, 15],
                                     [6, 13, 13, 10, 9, 19, 7, 24, 23, 16],
                                     [7, 24, 23, 10, 18, 24, 17],
                                     [10, 25, 18, 6, 1, 19, 4],
                                     [19, 14, 6, 2, 19, 6, 9, 1, 19, 4],
                                     [10, 14, 17, 6, 21, 10, 9, 24, 17],
                                     [4, 5, 10, 22, 25],
                                     [1, 12, 24, 25],
                                     [14, 1, 25, 10, 25, 20, 10]],
                 'solution': dict(zip(range(1, 27), "oqhspirktajvmbgydxuzcwlenf"))},

            15: {'given_letters': {5: 'l', 9: 'd', 25: 'w'},
                 'encoded_words': [[13, 5, 9],
                                   [14, 11, 12, 6, 6],
                                   [14, 19, 5],
                                   [12, 13, 25, 19, 24],
                                   [8, 6, 18, 11, 6, 4, 21],
                                   [3, 5, 13, 15, 2],
                                   [3, 1, 23, 23, 26],
                                   [21, 7, 12, 13, 8],
                                   [4, 25, 1, 12, 5, 6, 9],
                                   [22, 19, 4, 15, 19, 12, 19],
                                   [6, 24, 21, 6, 12],
                                   [10, 6, 12, 2, 26],
                                   [3, 5, 11, 1, 9],
                                   [8, 12, 19, 17, 19, 9, 13],
                                   [3, 11, 9, 16, 6],
                                   [6, 26, 6],
                                   [2, 1, 21, 21, 26],
                                   [26, 6, 21],
                                   [13, 11, 12, 4],
                                   [9, 19, 25, 9, 5, 6, 12],
                                   [14, 19, 24, 1, 15],
                                   [12, 11, 8, 26],
                                   [6, 20, 18, 11, 1, 4, 1, 21, 6],
                                   [14, 12, 6, 21, 23, 6, 5],
                                   [5, 13, 21, 7],
                                   [4, 21, 11, 22, 14],
                                   [8, 5, 19, 15, 2, 10, 19, 15, 2],
                                   [11, 4, 11, 19, 5],
                                   [19, 9, 13, 12, 24],
                                   [8, 5, 19, 15, 2, 10, 19, 15, 2],
                                   [4, 6, 6, 14, 19, 16, 6],
                                   [21, 7, 1, 12, 9, 5, 26],
                                   [19, 8, 5, 6],
                                   [3, 13, 24, 21],
                                   [5, 13, 3, 21, 26],
                                   [17, 6, 24, 21]],
                  'solution': dict(zip(range(1, 27), "ikfslehbdjuropcgvqaxtmznwy"))},
            
            19: {'given_letters': {6: 't', 14: 'r', 26: 'u'},
                 'encoded_words': [[21, 14, 13, 25, 13, 25],
                                   [25, 26, 21, 16],
                                   [24, 14, 7, 13, 6],
                                   [10, 18, 20, 6, 24, 24, 3],
                                   [20, 8, 13, 11],
                                   [25, 5, 19, 26, 5, 3, 21, 5],
                                   [14, 20, 10, 6, 26, 14, 24, 26, 25],
                                   [7, 24, 20],
                                   [8, 13, 5],
                                   [21, 4, 5, 19, 26, 5, 14, 5, 11],
                                   [5, 2, 5, 25, 13, 12, 4, 6],
                                   [22, 26, 11, 24],
                                   [21, 4, 20, 3, 3, 5, 18],
                                   [17, 4, 13, 23, 23],
                                   [16, 5, 5, 18],
                                   [11, 5, 12, 14, 5, 5],
                                   [14, 20, 7, 7, 13],
                                   [25, 5, 6, 6],
                                   [25, 26, 10, 14, 5, 15, 24],
                                   [25, 6, 20, 6, 26, 5, 25, 19, 26, 5],
                                   [21, 14, 24, 17, 3],
                                   [25, 24, 2, 20],
                                   [24, 3, 21, 5],
                                   [8, 13, 20],
                                   [21, 24, 24],
                                   [9, 26, 3, 21, 6, 13, 24, 3, 20, 18],
                                   [14, 5, 8],
                                   [10, 13, 5],
                                   [7, 20, 14],
                                   [20, 11, 11],
                                   [13, 21, 2],
                                   [5, 1, 4, 20, 18, 5, 11],
                                   [5, 3, 11],
                                   [5, 20, 21, 4],
                                   [5, 14, 20, 25, 5],
                                   [26, 3, 13, 6, 5],
                                   [24, 24, 23, 5],
                                   [25, 17, 13, 12]],
                  'solution': dict(zip(range(1, 27), "xynhetbvfpdgirmkwlqacjzosu"))}

}



