from spm.__wrapper__ import Runtime


def spm_csd_int_IS(*args, **kwargs):
    """
      Wrapper for erp and csd response of a neural mass model  
        FORMAT [y] = spm_csd_int_IS(P,M,U)  
         
        P - parameters  
        M - neural mass model structure  
        U - time-dependent input  
         
        y{1}  - erp  
        y{2}  - csd  
       __________________________________________________________________________  
         
        This integration routine evaluates the responses of a neural mass model  
        to exogenous input - in terms of neuronal states. These are then used as  
        expansion point to generate complex cross spectral responses due to  
        random neuronal fluctuations. The ensuing spectral (induced) response is  
        then convolved (in time) with a window that corresponds to the window of  
        a standard wavelet transform. In other words, this routine generates  
        predictions of data features based upon a wavelet transform  
        characterisation of induced responses.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_csd_int_IS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_int_IS", *args, **kwargs)
