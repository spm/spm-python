from spm._runtime import Runtime


def spm_fnirs_viewer_sensor(*args, **kwargs):
    r"""
      Display optode/channel positions on the rendered brain surface  
          
        FORMAT spm_fnirs_viewer_sensor(R)  
         
        R - structure array containing optode/channel positions   
           - This structure can be obtained using the SPM-fNIRS toolbox  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_fnirs/spm_fnirs_viewer_sensor.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fnirs_viewer_sensor", *args, **kwargs, nargout=0)
