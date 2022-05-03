#!/usr/bin/env python3
# -*- coding: utf-8 -*-

YourName = input('Your Name is: ');
NowYourScore = int(input('Now Your score is: '));
PastYourScore = int(input('Your past score is: '));
r = '{:.2%}'.format((NowYourScore-PastYourScore)/PastYourScore);

print("亲爱的 %s, 你本次的成绩是 %d, 你上次的成绩是 %d, 相比于上次, 你的分数进步了 %s." % (YourName, NowYourScore, PastYourScore, r));

print(f"亲爱的{YourName}, 你本次的成绩是{NowYourScore}, 你上次的成绩是{PastYourScore}, 相比于上次, 你的分数进步了{r}.");