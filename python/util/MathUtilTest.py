import MathUtil
import NumpyUtil

datas = [0.16, -0.67, -0.21, 0.54, 0.22, -0.15, -0.63, 0.03, 0.88, -0.04, 0.20, 0.52, -1.03, 0.11, 0.49, -0.47, 0.35,
         0.80, -0.33, -0.24, -0.13, -0.82, 0.56]

print(MathUtil.get_avg(datas))
print(NumpyUtil.get_avg(datas))
print(MathUtil.get_vari(datas))
print(NumpyUtil.get_vari(datas))
print(MathUtil.get_std_dev(datas))
print(NumpyUtil.get_std_dev(datas))

datas_sh000300 = [0.16, -0.67, -0.21, 0.54, 0.22, -0.15, -0.63, 0.03, 0.88, -0.04, 0.20, 0.52, -1.03, 0.11, 0.49, -0.47,
                  0.35, 0.80, -0.33, -0.24, -0.13, -0.82, 0.56]

datas_sz000651 = [0.07, -0.55, -0.04, 3.11, 0.28, -0.50, 1.10, 1.97, -0.31, -0.55, 2.06, -0.24, -1.44, 1.56, 3.69, 0.53,
                  2.30, 1.09, -2.63, 0.29, 1.30, -1.54, 3.19]

print(MathUtil.get_cov(datas_sh000300, datas_sz000651))
print(NumpyUtil.get_cov(datas_sh000300, datas_sz000651))
