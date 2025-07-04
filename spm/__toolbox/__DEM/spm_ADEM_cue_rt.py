from spm._runtime import Runtime


def spm_ADEM_cue_rt(*args, **kwargs):
    """
      returns reaction times and accuracy for ADEM_cued_response demo  
        FORMAT [on,rt,ac] = spm_ADEM_cue_rt(DEM)  
         
        DEM - DEM structure from ADEM_cued_response.m  
         
        on  - cue onset  
        ac  - accuracy  
        rt  - reaction time  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_ADEM_cue_rt.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ADEM_cue_rt", *args, **kwargs)
