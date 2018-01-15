#!/usr/bin/env python
"""Generate passwords that are fun to type"""
from __future__ import print_function
from os import urandom

def choice(keys):
    """Uniformly choose element from list keys, note len(keys) must be
    less than 256"""
    while(True):
        i = ord(urandom(1))
        if i < 256 - (256 % len(keys)):
            return keys[i % len(keys)]

# QWERTY layout:
left_keys_q = [["`", "1", "2", "3", "4", "5", "6", ],
               ["q", "w", "e", "r", "t", ],
               ["a", "s", "d", "f", "g", ],
               ["z", "x", "c", "v", ], ]
left_shift_q = [["~", "!", "@", "#", "$", "%", "^", ],
                ["Q", "W", "E", "R", "T", ],
                ["A", "S", "D", "F", "G", ],
                ["Z", "X", "C", "V", ], ]

right_keys_q = [["7", "8", "9", "0", "-", "="],
                ["y", "u", "i", "o", "p", "[", "]", "\\", ],
                ["h", "j", "k", "l", ";", "'", ],
                ["b", "n", "m", ",", ".", "/", ], ]
right_shift_q = [["&", "*", "(", ")", "_", "+", ],
                 ["Y", "U", "I", "O", "P", "{", "}", "|", ],
                 ["H", "J", "K", "L", ":", "\"", ],
                 ["B", "N", "M", "<", ">", "?", ], ]

# Dvorak layout:
left_keys_d = [["`", "1", "2", "3", "4", "5", "6", ],
               ["'", ",", ".", "p", "y", ],
               ["a", "o", "e", "u", "i", ],
               [";", "q", "j", "k", ], ]
left_shift_d = [["~", "!", "@", "#", "$", "%", "^", ],
                ["\"", "<", ">", "P", "Y", ],
                ["A", "O", "E", "U", "I", ],
                [":", "Q", "J", "K", ], ]

right_keys_d = [["7", "8", "9", "0", "[", "]"],
                ["f", "g", "c", "r", "l", "/", "=", "\\", ],
                ["d", "h", "t", "n", "s", "-", ],
                ["x", "b", "m", "w", "v", "z", ], ]
right_shift_d = [["&", "*", "(", ")", "{", "}", ],
                 ["F", "G", "C", "R", "L", "?", "+", "|", ],
                 ["D", "H", "T", "N", "S", "_", ],
                 ["X", "B", "M", "W", "V", "Z", ], ]


def generate_password(length):
    """Generate a password"""

    # Alternating hands is fun
    password = ""

    # choose randomly which hand to lead
    hand = choice(["left", "right"])

    # choose randomly whether to start with shift
    # note that the state of `shift` is a Markov chain with stationary
    # distribution (0.5, 0.5), so draw from the stationary distribution so
    # that the probability of shift being True or False at any given point
    # in the algorithm is 0.5
    shift = choice([True, False])

    for i in range(length):
        if hand == "left":
            # Choose whether shift key
            if shift:
                password += choice([k for l in right_shift_d for k in l])
                shift = False
                hand = "left"
            else:
                password += choice([k for l in left_keys_d for k in l])
                shift = choice([True, False])
                hand = "right"
        elif hand == "right":
            # Choose whether shift key
            if shift:
                password += choice([k for l in left_shift_d for k in l])
                shift = False
                hand = "right"
            else:
                password += choice([k for l in right_keys_d for k in l])
                shift = choice([True, False])
                hand = "left"

    return password


if __name__ == '__main__':
    password = generate_password(14)
    print(password)
