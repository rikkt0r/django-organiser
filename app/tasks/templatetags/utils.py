from django import template

register = template.Library()


@register.filter
def get_range(value):
    return [v + 1 for v in range(value)]


@register.filter
def partition(thelist, n):
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = len(thelist) / n
    return [thelist[p * i:p * (i + 1)] for i in range(n - 1)] + [thelist[p * (i + 1):]]


@register.filter
def part2(thelist):
    try:
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]

    p = int(len(thelist) / 2)

    if len(thelist) == 2:
        return [thelist[0], thelist[1]]
    elif p % 2:
        return [
            thelist[0:p+1],
            thelist[p+1:]
        ]
    else:
        return [
            thelist[0:p],
            thelist[p:]
        ]


@register.filter
def partition_horizontal(thelist, n):
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    newlists = [list() for i in range(n)]
    for i, val in enumerate(thelist):
        newlists[i % n].append(val)
    return newlists


@register.filter
def length(thelist):
    try:
        return len(thelist)
    except (ValueError, TypeError):
        return 0
