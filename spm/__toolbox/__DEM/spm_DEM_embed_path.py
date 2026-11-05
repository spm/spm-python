from spm._runtime import Runtime


def spm_DEM_embed_path(*args, **kwargs):
    r"""
      Temporal embedding into generalised coordinates of motion  
        FORMAT [y] = spm_DEM_embed_path(Y,n,t,dt)  
       __________________________________________________________________________  
        Y    - (v x N) matrix of v time-series of length N  
        n    - order of temporal embedding  
        t    - time  {bins} at which to evaluate derivatives (starting at t = 1)  
        dt   - sampling interval {secs} [default = 1]  
         
        y    - {n,1}(v x 1) temporal derivatives   y[:] <- E*Y(t)  
       __________________________________________________________________________  
        see also spm_DEM_embed. This version uses slightly different boundary  
        conitions  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_DEM_embed_path.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_embed_path", *args, **kwargs)
