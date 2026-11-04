from spm._runtime import Runtime


def spm_beamforming(*args, **kwargs):
    r"""
      GUI gateway to Beamforming toolbox  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/spm_beamforming.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_beamforming", *args, **kwargs, nargout=0)
