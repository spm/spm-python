from spm._runtime import Runtime


def spm_srender(*args, **kwargs):
    r"""
      A function for rendering surfaces  
        FORMAT spm_srender(job)  
        job - a job structure (see tbx_cfg_render.m)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/SRender/spm_srender.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_srender", *args, **kwargs, nargout=0)
