from spm._runtime import Runtime


def spm_DEM_embed(*args, **kwargs):
    r"""
      Temporal embedding into generalised coordinates of motion  
        FORMAT [y] = spm_DEM_embed(Y,n,t,dt,d)  
       __________________________________________________________________________  
        Y    - (v x N) matrix of v time-series of length N  
        n    - order of temporal embedding  
        t    - time  {bins} at which to evaluate derivatives (starting at t = 1)  
        dt   - sampling interval {secs} [default = 1]  
        d    - delay (bins) for each row of Y  
         
        y    - {n,1}(v x 1) temporal derivatives   y[:] <- E*Y(t)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_embed.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_embed", *args, **kwargs)
