#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'abandon':1, 'abstract':2,'action':3};
print(d['action']);
d['action'] = 4;
print(d)
print('action' in d);
d.pop('action');
print('action' in d);
n = set([1, 2, 3]);
print(n);
n.add('4');
print(n);
n.remove(1);
print(n);
print(d & n);
print(d | n);