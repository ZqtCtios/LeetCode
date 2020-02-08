class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        al = int(a.split('+')[0])
        ar = int(a.split('+')[1][:-1])
        bl = int(b.split('+')[0])
        br = int(b.split('+')[1][:-1])
        xl = al*bl-ar*br
        xr = al*br+bl*ar
        s = '{}+{}i'.format(xl, xr)
        return s
