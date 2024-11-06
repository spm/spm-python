from spm.__wrapper__ import Runtime


def spm_gx_adem_cue(*args, **kwargs):
    """
      returns the prediction for cued responses (proprioception and vision)  
        FORMAT [g]= spm_gx_adem_cue(x,v,a,P)  
         
        x    - hidden states:  
          x.o  - intrinsic motor state (proprioceptive)  
         
        v    - hidden causes  
         
        P    - target locations (visual) - extrinsic coordinates (Cartesian)  
         
        g    - sensations:  
          g.o  - motor angle (proprioception)  
          g.p  - finger location (visual)  
          g.c  - target contrast (visual)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_gx_adem_cue.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_adem_cue", *args, **kwargs)
