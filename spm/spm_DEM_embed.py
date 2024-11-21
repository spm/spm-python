from spm.__wrapper__ import Runtime


def spm_DEM_embed(*args, **kwargs):
    """
      Temporal embedding into derivatives  
        FORMAT [y] = spm_DEM_embed(Y,n,t,dt,d)  
       __________________________________________________________________________  
        Y    - (v x N) matrix of v time-series of length N  
        n    - order of temporal embedding  
        t    - time  {bins} at which to evaluate derivatives (starting at t = 1)  
        dt   - sampling interval {secs} [default = 1]  
        d    - delay (bins) for each row of Y  
         
        y    - {n,1}(v x 1) temporal derivatives   y[:] <- E*Y(t)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_embed.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_embed", *args, **kwargs)
