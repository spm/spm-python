from spm.__wrapper__ import Runtime


def spm_csd_fmri_mar(*args, **kwargs):
    """
      Prediction of MAR coefficients for DCM  
        FORMAT [y,S,K] = spm_csd_fmri_mar(P,M,U)  
         
        P - model parameters  
        M - model structure  
        U - model inputs (expects U.csd as complex cross spectra)  
         
        y - y(nw,nn,nn} - cross-spectral density for nn nodes  
                        - for nw frequencies in M.Hz  
        K - Volterra kernels  
        S - directed transfer functions (complex)  
         
        This routine computes the spectral response of a network of regions  
        driven by  endogenous fluctuations and exogenous (experimental) inputs.  
        It returns the complex cross spectra of regional responses as a  
        three-dimensional array. The endogenous innovations or fluctuations are  
        parameterised in terms of a (scale free) power law, in frequency space.  
         
        When the observer function M.g is specified, the CSD response is  
        supplemented with observation noise in sensor space; otherwise the CSD  
        is noiseless.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_csd_fmri_mar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_fmri_mar", *args, **kwargs)
