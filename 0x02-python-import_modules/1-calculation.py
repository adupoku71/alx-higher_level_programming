#!/usr/bin/python3
import calculator_1 as calc


if __name__ == "__main__":
    a = 10
    b = 5

    # add function call
    print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))

    # sub function call
    print("{:d} + {:d} = {:d}".format(a, b, calc.sub(a, b)))

    # mul function call
    print("{:d} + {:d} = {:d}".format(a, b, calc.mul(a, b)))

    # div function call
    print("{:d} + {:d} = {:d}".format(a, b, calc.div(a, b)))
