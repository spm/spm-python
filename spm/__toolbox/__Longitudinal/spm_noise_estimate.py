from spm._runtime import Runtime


def spm_noise_estimate(*args, **kwargs):
    r"""
      Estimate average noise from a series of images  
        FORMAT [noise,mu_val,info] = spm_noise_estimate(scans,K)  
        scans  - nifti objects or filenames of images  
        K      - number of Rician mixture components  
         
        noise  - standard deviation estimate  
        mu_val - expectation of more intense Rician  
        info   - This struct can be used for plotting the fit as:  
                     plot(info.x(:),info.p,'--',info.x(:), ...  
                          info.h/sum(info.h)/info.md,'b.', ...  
                          info.x(:),info.lse,'r');  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Longitudinal/spm_noise_estimate.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_noise_estimate", *args, **kwargs)
