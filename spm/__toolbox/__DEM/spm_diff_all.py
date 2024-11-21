from spm.__wrapper__ import Runtime


def spm_diff_all(*args, **kwargs):
    """
      matrix high-order numerical differentiation  
        FORMAT [dfdx] = spm_diff(f,x,...,n)  
        FORMAT [dfdx] = spm_diff(f,x,...,n,V)  
        FORMAT [dfdx] = spm_diff(f,x,...,n,'q')  
         
        f      - [inline] function f(x{1},...)  
        x      - input argument[s]  
        n      - arguments to differentiate w.r.t.  
         
        V      - cell array of matrices that allow for differentiation w.r.t.  
        to a linear transformation of the parameters: i.e., returns  
          
        df/dy{i};    x = V{i}y{i};    V = dx(i)/dy(i)  
         
        q      - flag to preclude default concatenation of dfdx  
         
        dfdx          - df/dx{i}                     ; n =  i  
        dfdx{p}...{q} - df/dx{i}dx{j}(q)...dx{k}(p)  ; n = [i j ... k]  
         
         
        - a cunning recursive routine  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_diff_all.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_diff_all", *args, **kwargs)
