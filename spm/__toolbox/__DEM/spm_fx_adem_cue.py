from spm.__wrapper__ import Runtime


def spm_fx_adem_cue(*args, **kwargs):
    """
      returns the flow for cued response (with action)  
        FORMAT [f]= spm_fx_adem_cue(x,v,a,P)  
         
        x    - hidden states:  
          x.o  - motor angle  
         
        v    - hidden causes  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_adem_cue.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_adem_cue", *args, **kwargs)
