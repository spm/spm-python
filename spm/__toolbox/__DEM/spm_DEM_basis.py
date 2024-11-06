from spm.__wrapper__ import Runtime


def spm_DEM_basis(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_basis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_basis", *args, **kwargs)
