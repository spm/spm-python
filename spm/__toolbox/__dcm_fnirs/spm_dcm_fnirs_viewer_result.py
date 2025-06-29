from spm._runtime import Runtime


def spm_dcm_fnirs_viewer_result(*args, **kwargs):
    """
      GUI for displaying DCM-fNIRS results  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_dcm_fnirs_viewer_result.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_fnirs_viewer_result", *args, **kwargs)
