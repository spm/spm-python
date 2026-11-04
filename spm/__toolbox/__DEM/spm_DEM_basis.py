from spm._runtime import Runtime


def spm_DEM_basis(*args, **kwargs):
    r"""
      evaluates a parameterized set of basis functions  
        problem  
        FORMAT [f,p] = spm_DEM_basis(x,v,P)  
         
        x   - hidden states  
        v   - causal inputs  
        P   - parameters  
         
        f   - f(x)  
        p   - p(i)  
         
        returns:  
          f = sum(P(i)*B(x,i))  
          P = p/sum(p)  
         
        where B(x,i) are basis functions  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_DEM_basis.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_basis", *args, **kwargs)
