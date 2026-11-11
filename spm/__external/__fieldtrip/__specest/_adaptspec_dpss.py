from spm._runtime import Runtime


def _adaptspec_dpss(*args, **kwargs):
    r"""
      ADAPTSPEC_DPSS Adaptive multitaper spectrum estimate  
         
          [spec, se, wt] = adaptspec_dpss(yk, sk, lambda, adaptflag)  
         
        Inputs  
          yk     : [nchan x nfft x ntap] complex, tapered data Fourier transforms  
          lambda   : [ntap x 1] real, eigenvalues of DPSS tapers  
          adaptflag : integer, mode (default=0)  
                   0 - unweighted average (all tapers equal)  
                   1 - weighted by eigenvalues  
                   2 - adaptive multitaper (Thomson)  
         
        Outputs  
          spec : [nchan x nfft] spectrum estimate  
          se   : [1 x nfft] effective degrees of freedom  
          wt   : [nchan x nfft x ntap] weights applied to tapers  
         
        Notes  
        - Follows German Prieto’s code (https://github.com/gaprieto/multitaper).  
        - The adaptive scheme iterates until convergence or max mloop.  
        - ChatGPT provided a rough translation from Python to MATLAB, code  
        optimized for MATLAB + multichannel data by JMS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/specest/private/adaptspec_dpss.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("adaptspec_dpss", *args, **kwargs)
