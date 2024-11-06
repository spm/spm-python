from spm.__wrapper__ import Runtime


def spm_fx_poly(*args, **kwargs):
    """
      Normal (bilinear) form equation of motion  
        FORMAT [f] = spm_fx_poly(x,v,P)  
        x      - state vector  
        v      - exogenous cause  
        P      - free parameters  
         
        f      - dx/dt  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fx_poly.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_poly", *args, **kwargs)
