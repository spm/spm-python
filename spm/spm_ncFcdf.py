from spm.__wrap__ import _Runtime


def spm_ncFcdf(*args, **kwargs):
  """  Cumulative Distribution Function (CDF) of non-central F-distribution  
    FORMAT f = spm_ncFcdf(x,df,d)  
    x  - F-variate (F has range [0,Inf) )  
    df - degrees of freedom, df = [v,w] with v>0 and w>0  
    d  - non-centrality parameter  
    F  - CDF of non-central F-distribution with [v,w] d.f. at points x  
     
    Reference:  
    https://en.wikipedia.org/wiki/Noncentral_F-distribution  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ncFcdf.m)
  """

  return _Runtime.call("spm_ncFcdf", *args, **kwargs)
