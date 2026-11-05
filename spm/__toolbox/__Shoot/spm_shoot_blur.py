from spm._runtime import Runtime


def spm_shoot_blur(*args, **kwargs):
    r"""
      A function for blurring ("smoothing") tissue probability maps  
        FORMAT [sig,a_new] = spm_shoot_blur(t,prm,its,sig)  
            t   - sufficient statistics  
            prm - regularisation parameters (1,1,1, 0.01,0.02,1)  
            its - max no. iterations (12)  
            sig - optional starting estimates (ignored for now)  
         
            sig - "smoothed" average  
            a   - parameters  
         
        The core of this procedure is described in:  
            John Ashburner & Karl J. Friston.  
            "Computing Average Shaped Tissue Probability Templates"  
            Neuroimage. 2009 Apr 1;45(2):333-41.  
         
        However, there is an additional modification such that the the null space  
        of the parameters is rotated out.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Shoot/spm_shoot_blur.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_shoot_blur", *args, **kwargs)
