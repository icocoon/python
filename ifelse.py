#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 小明身高 1.75，体重 80.5kg。请根据 BMI 公式（体重除以身高的平方）帮小明计算他的 BMI 指数，并根据 BMI 指数：

# 低于 18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于 32：严重肥胖


YourHight = float(input("please input your hight(m): "));
YourWeight = float(input("please input your weight(kg): "));
YourBMI = YourWeight / (YourHight * YourHight);


if YourBMI >= 32:
    print(f'您的 BMI 为{YourBMI}, 严重肥胖' );
elif 28 <= YourBMI < 32:
    print(f'您的 BMI 为{YourBMI}, 肥胖');
elif 25 <= YourBMI < 28:
    print(f'您的 BMI 为{YourBMI}, 过重');
elif 18.5 <= YourBMI < 25:
    print(f'您的 BMI 为{YourBMI}, 正常');
else:
    print(f'您的 BMI 为{YourBMI}, 过轻');