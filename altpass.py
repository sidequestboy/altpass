#!/usr/bin/env python3
"""Generate passwords that are fun to type"""
from os import urandom

def choice(keys):
    """Uniformly choose element from list keys, note len(keys) must be
    less than 256"""
    while(True):
        i = int.from_bytes(urandom(1), byteorder='big')
        if i < 256 - (256 % len(keys)):
            return keys[i % len(keys)]

# QWERTY layout:
left_keys = [["`", "1", "2", "3", "4", "5", "6", ],
             ["q", "w", "e", "r", "t", ],
             ["a", "s", "d", "f", "g", ],
             ["z", "x", "c", "v", ], ]
left_shift = [["~", "!", "@", "#", "$", "%", "^", ],
              ["Q", "W", "E", "R", "T", ],
              ["A", "S", "D", "F", "G", ],
              ["Z", "X", "C", "V", ], ]

right_keys = [["7", "8", "9", "0", "-", "="],
              ["y", "u", "i", "o", "p", "[", "]", "\\", ],
              ["h", "j", "k", "l", ";", "'", ],
              ["b", "n", "m", ",", ".", "/", ], ]
right_shift = [["&", "*", "(", ")", "_", "+", ],
               ["Y", "U", "I", "O", "P", "{", "}", "|", ],
               ["H", "J", "K", "L", ":", "\"", ],
               ["B", "N", "M", "<", ">", "?", ], ]


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
                password += choice([k for l in right_shift for k in l])
                shift = False
                hand = "left"
            else:
                password += choice([k for l in left_keys for k in l])
                shift = choice([True, False])
                hand = "right"
        elif hand == "right":
            # Choose whether shift key
            if shift:
                password += choice([k for l in left_shift for k in l])
                shift = False
                hand = "right"
            else:
                password += choice([k for l in right_keys for k in l])
                shift = choice([True, False])
                hand = "left"

    return password


if __name__ == '__main__':
    password = generate_password(14)
    print(password)
