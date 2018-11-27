def printer_error(s):
    return "%d/%d" % (sum([0 if x in "abcdefghijklm" else 1 for x in s]), len(s))

s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
assert(printer_error(s)=="3/56")