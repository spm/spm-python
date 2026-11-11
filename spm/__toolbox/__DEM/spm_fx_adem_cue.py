from spm._runtime import Runtime


def spm_fx_adem_cue(*args, **kwargs):
    r"""
      returns the flow for cued response (with action)  
        FORMAT [f]= spm_fx_adem_cue(x,v,a,P)  
         
        x    - hidden states:  
          x.o  - motor angle  
         
        v    - hidden causes  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_adem_cue.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_adem_cue", *args, **kwargs)
