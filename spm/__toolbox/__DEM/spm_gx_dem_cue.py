from spm._runtime import Runtime


def spm_gx_dem_cue(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_gx_dem_cue.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_dem_cue", *args, **kwargs)
