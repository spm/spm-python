from spm.__wrapper__ import Runtime


def spm_dpss(*args, **kwargs):
  """  Compute discrete prolate spheroidal sequences  
    FORMAT [E] = spm_dpss (N,NW)  
     
    N         Length of taper  
    NW        Product of N and W  
      
    E         [N x 2NW] matrix containing dpss sequences  
              The kth column contains the sequence which  
              comprises the length N signal that is kth most   
              concentrated in the frequency band |w|<=2*pi*W radians   
     
    See Section 8.3 in  
        Percival, D.B. and Walden, A.T., "Spectral Analysis For Physical  
        Applications", Cambridge University Press, 1993.   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_dpss.m)
  """

  return Runtime.call("spm_dpss", *args, **kwargs)
