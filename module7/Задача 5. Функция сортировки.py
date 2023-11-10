def tpl_sort(tpl):
    if all(isinstance(elem, int) for elem in tpl):
        return sorted(tpl)
    return tpl


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))