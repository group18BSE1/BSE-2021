try:
    def function(c, r, n, t):
        P = c*(1 + r/n)**(t * n)
        return P

    # the arguments are arranged in the same order as defined in the function

    R = function(1000, 0.01, 1, 1.0)
    print(round(R, 2))
except ValueError:
    print("Enter only digits not words")

