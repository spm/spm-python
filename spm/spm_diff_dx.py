from spm.__wrapper__ import Runtime


def spm_diff_dx(*args, **kwargs):
    """
      Optimisation of finite difference for numerical differentiation  
        FORMAT [dx] = spm_diff_dx(f,x,...,n)  
        FORMAT [dx] = spm_diff_dx(f,x,...,n,V)  
        FORMAT [dx] = spm_diff_dx(f,x,...,n,'q')  
         
        f      - [inline] function f(x{1},...)  
        x      - input argument[s]  
        n      - arguments to differentiate w.r.t.  
         
        dx     - 'best' step size  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_diff_dx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_diff_dx", *args, **kwargs)
