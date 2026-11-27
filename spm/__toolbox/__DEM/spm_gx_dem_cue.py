from spm._runtime import Runtime


def spm_gx_dem_cue(*args, **kwargs):
    r"""
      returns the prediction for cued responses (proprioception and vision)  
        FORMAT [g]= spm_gx_dem_cue(x,v,P)  
         
        x    - hidden states:  
          x.o  - intrinsic motor state (proprioceptive)  
          x.a  - target salience (attractiveness)  
         
        v    - hidden causes  
         
        P.x  - target locations (visual) - extrinsic coordinates (Cartesian)  
         
        g    - sensations:  
          g.o  - motor angle (proprioception)  
          g.p  - finger locations (visual)  
          g.c  - target contrast  (visual)  
          
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_gx_dem_cue.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_dem_cue", *args, **kwargs)
