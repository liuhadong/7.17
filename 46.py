def USDOL(rmb):
    dol = 6.28
    rmb1 = rmb*dol
    return('折合人民币:%.2f'%rmb1)
print(USDOL(float(input('请输入美元金额:'))))



