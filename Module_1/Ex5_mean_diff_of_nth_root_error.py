def md_nre_single_sample(y, yhat, n, p):
    result = (y**(1/n) - yhat**(1/n))**p
    print(result)

md_nre_single_sample(100, 99.5, 2, 1)
md_nre_single_sample(50, 49.5, 2, 1)
md_nre_single_sample(20, 19.5, 2, 1)
md_nre_single_sample(0.6, 0.1, 2, 1)