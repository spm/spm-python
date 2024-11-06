from spm.__wrapper__ import Runtime


def spm_ccf2coh(*args, **kwargs):
    """
      Converts cross covariance function to coherence  
        FORMAT [coh] = spm_ccf2coh(ccf,Hz)  
         
        ccf  (N,:,:)  - cross covariance functions  
        Hz   (n x 1)  - vector of frequencies (Hz)  
         
        coh           - coherence  
         
        See also: spm_???2???.m  
            ??? = {'ccf','csd','gew','mar','coh','mtf','ker','ssm','dcm'}  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ccf2coh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ccf2coh", *args, **kwargs)
