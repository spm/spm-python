from spm._runtime import Runtime


def spm_fx_dem_cue(*args, **kwargs):
    r"""
      returns the flow for cued response  
        FORMAT [f]= spm_fx_dem_cue(x,v,P)  
         
        x    - hidden states:  
          x.o  - intrinsic motor state (proprioceptive)  
          x.a  - target salience (attractiveness)  
         
        v    - hidden causes  
         
        P.x  - target locations (visual) - extrinsic coordinates (Cartesian)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_dem_cue.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_dem_cue", *args, **kwargs)
