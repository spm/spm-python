from spm.__wrap__ import _Runtime


def spm_DEM_embed(*args, **kwargs):
  """  Temporal embedding into derivatives  
    FORMAT [y] = spm_DEM_embed(Y,n,t,dt,d)  
   __________________________________________________________________________  
    Y    - (v x N) matrix of v time-series of length N  
    n    - order of temporal embedding  
    t    - time  {bins} at which to evaluate derivatives (starting at t = 1)  
    dt   - sampling interval {secs} [default = 1]  
    d    - delay (bins) for each row of Y  
     
    y    - {n,1}(v x 1) temporal derivatives   y[:] <- E*Y(t)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DEM_embed.m)
  """

  return _Runtime.call("spm_DEM_embed", *args, **kwargs)
