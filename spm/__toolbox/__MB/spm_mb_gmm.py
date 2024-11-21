from spm.__wrapper__ import Runtime


def spm_mb_gmm(*args, **kwargs):
    """
       
        FORMAT varargout = spm_mb_gmm(varargin)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_gmm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mb_gmm", *args, **kwargs)
