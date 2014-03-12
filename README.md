# AltPass
Generate a password:

```
$ python altpass.py
FhvWu+zT[+2!-:
```

The principle here is that the passphrase can be typed on a QWERTY keyboard alternating hands each stroke, which is a nice memory trick, and fun to do.

## Entropy Benchmarks
The passphrases generated have log2(1092/47)~4.5 bits of entropy per character.

A completely random password on the same character set has log2(94)~6.55 bits per character

A randomly selected English phrase has ~ 1 bit per character ([Shannon 1948][1])

An [xkcd password][1] has ~ 1.6 bits per character

## Randomness
The randomness is supplied by your operating system's urandom. This ought to be cryptographically secure.

## How many characters should you use?
Apparently, the state of the art of cracking passwords is 300 billion guesses per second. So, we want our password space to be pretty big. With `n` bits of entropy, if someone were targetting you with this much power, it would take an average of `(300 billion)*2^(n-1)` seconds to crack your password.

In other terms, the probability of them cracking your password after `t` seconds is `(300 billion)*t / 2^n`. We can set this probability arbitrarily low for a given `t` with a sufficiently large number of bits, `n`.

Suppose we require that the probability of cracking before 6 months is less than 1%, then we should have `n = log2((300*10^9)*(6*30*24*60*60)/0.01)~69` bits of entropy in our password. In our algorithm's case, the corresponding number of characters is `c=n/4.5`, so 15 characters is sufficient in this case.

## I can't remember this password!
It just takes a little practice! However, maybe [xkcd passwords][2] are more your speed (about 3 times as many characters, but actual words!).

[1]: http://www.scribd.com/doc/166218043/Shannon-1948
[2]: https://github.com/beala/xkcd-password
