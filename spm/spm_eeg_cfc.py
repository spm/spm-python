from spm.__wrapper__ import Runtime


def spm_eeg_cfc(*args, **kwargs):
    """
      Compute GLM for phase-amplitude and amplitude-amplitude coupling  
        FORMAT spm_eeg_cfc(S)  
         
        Xamp = independent variable to be explained:  
               Xamp = B1*sin(Xphase) + B2*cos(Xphase) + B3*Xlowamp  
         
        Additional regressors may be included  
        - overall estimates of PAC & AMP are obtained from continuous (or  
          concatenated) data  
        - statistical inference of these estimates is performed by dividing the  
          continuous time series into shorter epochs  
        - function writes out images of the estimated PAC & AMP, as well as their  
          p-values  
       __________________________________________________________________________  
         
        References:  
        van Wijk et al. 2015 J Neurosci Methods  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_cfc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_cfc", *args, **kwargs, nargout=0)
