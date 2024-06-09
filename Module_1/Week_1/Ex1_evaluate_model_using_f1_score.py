def calc_f1_score(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
    elif not isinstance(fp, int):
        print("fp must be int")
    elif not isinstance(fn, int):
        print('fn must be int')
    elif tp < 0 or fp < 0 or fn < 0:
        print("tp and fp and fn must be greater than 0")
    else:
        precision = tp / (tp + fp)

        recall = tp / (tp + fn)

        f1_score = 2 * (precision * recall) / (precision + recall)

        print(f'precision is {precision}\nrecall is {recall}\nf1-score is {f1_score}')

calc_f1_score(tp = 2, fp = 4, fn = 5)

# Example
# calc_f1_score(tp='a', fp=3, fn=4)
# calc_f1_score(tp=2, fp='a', fn=4)
# calc_f1_score(tp=2, fp=3, fn='a')
# calc_f1_score(tp=2.1, fp=3, fn=0)