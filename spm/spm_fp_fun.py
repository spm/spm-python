from spm.__wrapper__ import Runtime


def spm_fp_fun(*args, **kwargs):
    """
      Return the predicted diffusion for Fokker Planck optimisation  
        FORMAT [y] = spm_fp_fun(P,M,U)  
         
        P = spm_vec(P)  
        P.a - 0th order coefficients of force  
        P.b - 1st order coefficients of force  
        P.c - 2nd order coefficients of force  
         
        M   - model specifying flow(M(1).f; density M(1).fq and support M(1).X  
        U   - inputs  
         
        y   - prediction  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fp_fun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fp_fun", *args, **kwargs)
