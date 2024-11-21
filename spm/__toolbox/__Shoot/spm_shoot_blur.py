from spm.__wrapper__ import Runtime


def spm_shoot_blur(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_blur.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_blur", *args, **kwargs)
