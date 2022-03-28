# 一维循环展开宏
# 1D loop unroll macro
unroll_size = 256

header_name = "MACRO_LOOP"

print("#ifndef {}_H".format(header_name))
print("#define {}_H".format(header_name))
print()
unroll_size += 1
code_str = """#define HELPER_{i1}(fun) HELPER_{i2}(fun); fun({i1})"""
print("#define HELPER_1(fun) fun(1);")
for i in range(2, unroll_size):
    para = {}
    para["i1"] = i
    para["i2"] = i-1
    print(code_str.format_map(para))
print("""#define HELPER(n, fun) HELPER_##n(fun)
#define LOOP(n, fun) HELPER(n, fun)""")

code_str = """#define HELPER2_{i1}(fun) HELPER2_{i2}(fun), fun({i1})"""
print("#define HELPER2_1(fun) fun(1)")
for i in range(2, unroll_size):
    para = {}
    para["i1"] = i
    para["i2"] = i-1
    print(code_str.format_map(para))
print("""#define HELPER2(n, fun) HELPER2_##n(fun)
#define LOOP_comma(n, fun) HELPER2(n, fun)""")
print()
print("#endif")
