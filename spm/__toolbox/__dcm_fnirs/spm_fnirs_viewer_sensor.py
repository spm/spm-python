from spm.__wrapper__ import Runtime


def spm_fnirs_viewer_sensor(*args, **kwargs):
    """
      Display optode/channel positions on the rendered brain surface  
          
        FORMAT spm_fnirs_viewer_sensor(R)  
         
        R - structure array containing optode/channel positions   
           - This structure can be obtained using the SPM-fNIRS toolbox  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_fnirs_viewer_sensor.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fnirs_viewer_sensor", *args, **kwargs, nargout=0)
