file_name_src = 'src.txt'
file_name_dst = 'dst.txt'
tmp = '{:<25}{:>5}\n'
all_avr = 0
all_st = 0

with open(file_name_src, 'rt', encoding='utf-8') as f_src:
    with open(file_name_dst, 'wt', encoding='utf-8') as f_dst:
        for line in f_src:
            line = line.split()
            name = line[1] + ' ' + line[0][0] + '.'
            avr = round(sum(int(x) for x in line[2:]) / len(line[2:]), 2)
            f_dst.write(tmp.format(name, avr))
            if avr < 5:
                print(tmp.format(name, avr), end='')
            all_st += 1
            all_avr += avr

print(tmp.format('Average by group:', round(all_avr / all_st, 2)))
