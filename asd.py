def round_figure(figure):
    n = 0
    figure_work = figure.__str__()

    for i in range(len(figure_work)):
        if figure_work[i] == '0':
            n += 1
        elif figure_work[i] == ',' or figure_work[i] == '.':
            pass
        elif figure_work[i] != '0':
            break
    print(n)
round_figure(11)

print(round(11.11), 1)

