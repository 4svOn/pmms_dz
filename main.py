import locale


def read_data(filename):
    file = open(filename)
    base = []
    for i in range(1, 978):
        str = file.readline()
        base.append(list(map(float, str.strip().split())))
    forecast = []
    for i in range(1, 51):
        str = file.readline()
        forecast.append(list(map(float, str.strip().split())))
        forecast[i - 1].append(977 + i)
    file.close()
    return base, forecast

def print_data(data, filename):
    file = open(filename, 'w')
    for f, pos in data:
        file.write(str(f) + ' ' + str(pos) + '\n')
    file.close()

def count_diff(f1, f2):
    diff = 0
    d = []
    for i1, p1 in f1:
        for i2, p2 in f2:
            if p1 == p2:
                diff += abs(i1 - i2)
                d.append([abs(i1 - i2), p1])
    return diff / 50, d

def print_diff(text, f1, f2, filename):
    lldiff, lld = count_diff(f1, f2)
    print(text, lldiff)
    lld.sort()
    lld.reverse()
    print_data(lld, filename)

def do_5_nomer(base):
    locale.setlocale(locale.LC_ALL, "ru_RU")
    c = 0.0
    while c <= 1.01:
        good_forecast = 0
        cnt = [0, 0]
        forecast = [0, 0]
        for recid, f in base:
            recid = int(recid)
            cnt[recid] += 1
            if recid == 1 and f >= c:
                forecast[1] += 1
            elif recid == 0 and f < c:
                forecast[0] += 1

        sensivity = forecast[1] / cnt[1]
        specificity = forecast[0] / cnt[0]
        print('c: ', locale.str(c), '   sensivity: ', locale.str(sensivity), '   specificity: ', locale.str(specificity))
        # print(locale.str(c), ';', locale.str(sensivity), ';',  locale.str(specificity))
        # print(locale.str(specificity))
        c += 0.05

def main():
    linear_b, linear_f = read_data("lin.txt")
    logit_b, logit_f = read_data("log.txt")
    probit_b, probit_f = read_data("proh.txt")
    linear_f.sort()
    linear_f.reverse()
    logit_f.sort()
    logit_f.reverse()
    probit_f.sort()
    probit_f.reverse()

    # print_data(linear_f, 'linear_forecast_sorted.txt')
    # print_data(logit_f, 'logit_forecast_sorted.txt')
    # print_data(probit_f, 'probit_forecast_sorted.txt')

    # print_diff('linear VS logit: ', linear_f, logit_f, 'linear_vs_logit.txt')
    # print_diff('linear VS probit: ', linear_f, probit_f, 'linear_vs_probit.txt')
    # print_diff('logit VS probit: ', logit_f, probit_f, 'logit_vs_probit.txt')

    do_5_nomer(logit_b)

# def fix():
#     w = open("lin.txt", 'w')
#     with open("linear_forecast.txt") as file:
#         for line in file:
#             line = line.replace(",", ".")
#             w.write(line)
#     w.close()

if __name__ == '__main__':
    main()

