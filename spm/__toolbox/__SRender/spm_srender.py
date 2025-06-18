from mpython import Runtime


def spm_srender(*args, **kwargs):
    """
      A function for rendering surfaces
        FORMAT spm_srender(job)
        job - a job structure (see tbx_cfg_render.m)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/SRender/spm_srender.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_srender", *args, **kwargs, nargout=0)
