zero = lambda f: lambda x: x
succ = lambda c: lambda f: lambda x: f(c(f)(x))
numerify = lambda c: c(lambda i: i + 1)(0)


def churchify(n):
    def _f(f):
        def _x(x):
            for i in range(n): x = f(x)
            return x

        return _x

    return _f


church_add = lambda c1: lambda c2: lambda f: lambda x: c1(f)(c2(f)(x))
church_mul = lambda c1: lambda c2: lambda f: lambda x: c1(c2(f))(x)
church_pow = lambda m: lambda n: lambda f: lambda x: n(m)(f)(x)
