from spm.__wrapper__ import Runtime


def spm_dartel_smooth(*args, **kwargs):
    """
      Smooth tissue probability maps  
        FORMAT [sig,a_new] = spm_dartel_smooth(t,lam,its,vx,a_old)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_smooth.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dartel_smooth", *args, **kwargs)
