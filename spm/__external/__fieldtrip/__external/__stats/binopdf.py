from spm.__wrap__ import _Runtime


def binopdf(*args, **kwargs):
  """  BINOPDF binomial probability density function  
     
    Y = BINOPDF(X,N,P) returns the binomial probability density  
    function with parameters N and P at the values in X.  
     
    See also BINOCDF and STATS (Matlab statistics toolbox)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/binopdf.m)
  """

  return _Runtime.call("binopdf", *args, **kwargs)
