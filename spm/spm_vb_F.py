from spm.__wrapper__ import Runtime


def spm_vb_F(*args, **kwargs):
    """
      Compute lower bound on evidence, F, for VB-GLM-AR models  
        FORMAT [F,Lav,KL] = spm_vb_F(Y,block)  
         
        Y             [T x N] time series   
        block         data structure (see spm_vb_glmar)  
         
        F             Lower bound on model evidence, F  
        Lav           Average Likelihood  
        KL            Kullback-Liebler Divergences with fields  
                      .w, .alpha, .beta, .Lambda, .a  
         
        This function implements equation 18 in paper VB4.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_F.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_F", *args, **kwargs)
