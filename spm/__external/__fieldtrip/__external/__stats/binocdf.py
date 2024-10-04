from spm.__wrap__ import _Runtime


def binocdf(*args, **kwargs):
  """  BINOCDF binomial cumulative distribution function  
     
    Y=BINOCDF(X,N,P) returns the binomial cumulative distribution  
    function with parameters N and P at the values in X.  
     
    See also BINOPDF and STATS (Matlab statistics toolbox)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/binocdf.m)
  """

  return _Runtime.call("binocdf", *args, **kwargs)
