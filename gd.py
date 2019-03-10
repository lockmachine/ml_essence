#!usr/bin/env python3
# coding: utf-8
import numpy as np

class GradientDescent:
    def __init__(self, f, df, alpha=0.01, eps=1e-6):
        self.f = f
        self.df = df
        self.alpha = alpha
        self.eps = eps
        self.path = None
        
    def solve(self, init):
        x = init
        path = []   # x がたどる経路
        grad = self.df(x)
        path.append(x)
        
        while (grad**2).sum() > self.eps**2:    # ∇f の L2 ノルムが eps 以下の時に終了する
            x = x - self.alpha * grad
            grad = self.df(x)
            path.append(x)
            #print('∇fのL2ノルム:{}\n'.format((grad**2).sum()), flush=True)
            
        self.path_ = np.array(path)
        self.x_ = x
        self.opt_ = self.f(x)
