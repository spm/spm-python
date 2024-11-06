from spm.__wrapper__ import Runtime


def spm_ddiff(*args, **kwargs):
    """
      Matrix high-order numerical differentiation (double stencil)  
        FORMAT [dfdx] = spm_ddiff(f,x,...,n)  
        FORMAT [dfdx] = spm_ddiff(f,x,...,n,V)  
        FORMAT [dfdx] = spm_ddiff(f,x,...,n,'q')  
         
        f      - [inline] function f(x{1},...)  
        x      - input argument[s]  
        n      - arguments to differentiate w.r.t.  
         
        V      - cell array of matrices that allow for differentiation w.r.t.  
        to a linear transformation of the parameters: i.e., returns  
         
        df/dy{i};    x = V{i}y{i};    V = dx(i)/dy(i)  
         
        q      - (char) flag to preclude default concatenation of dfdx  
         
        dfdx          - df/dx{i}                     ; n =  i  
        dfdx{p}...{q} - df/dx{i}dx{j}(q)...dx{k}(p)  ; n = [i j ... k]  
         
         
        This routine has the same functionality as spm_diff, however it  
        uses two sample points to provide more accurate numerical (finite)  
        differences that accommodate nonlinearities:  
         
        dfdx  = (4*f(x + dx) - f(x + 2*dx) - 3*f(x))/(2*dx)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ddiff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ddiff", *args, **kwargs)
