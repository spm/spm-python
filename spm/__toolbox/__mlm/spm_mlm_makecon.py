from spm.__wrapper__ import Runtime


def spm_mlm_makecon(*args, **kwargs):
    """
      Make contrast to test if the subset of coefficients indexed by w = 0 ?  
        FORMAT [con_vec] = spm_mlm_makecon (mlm,w)  
         
        mlm           MLM data structure containing  
                      [p x d] matrix of regression coefficients mlm.wmean  
        w             [p x d] matrix of comprising 1's and 0's with  
                      1s selecting the coefficients of interest  
         
        con_vec       Vectorised contrast matrix that can be passed   
                      to spm_mlm_posthoc.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mlm/spm_mlm_makecon.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mlm_makecon", *args, **kwargs)
