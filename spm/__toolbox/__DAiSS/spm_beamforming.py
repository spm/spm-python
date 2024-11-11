from spm.__wrapper__ import Runtime


def spm_beamforming(*args, **kwargs):
    """
      GUI gateway to Beamforming toolbox  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/spm_beamforming.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_beamforming", *args, **kwargs, nargout=0)
