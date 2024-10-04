from spm.__wrap__ import _Runtime


def spm_kmeans1(*args, **kwargs):
  """  K-means clustering for 1-dimensional data  
    FORMAT [mix1] = spm_kmeans1 (y,k)  
      
    y          [1 x N] data vector  
    k          Number of components  
     
    mix1       Returned model  
     
    -------------------------------------------------------------------------  
    The fields in mix1 are:  
    k                The number of components  
    m                Vector of means, m=[m_1,m_2,...,m_k]  
    v                Vector of variances, v=[v_1,v_2,..,v_k]  
    pi               Vector of mixing proportions, pi=[pi_1,pi_2,..,pi_k]  
    nloops           Number of iterations used  
    assign           Which class data points are assigned to  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mixture/spm_kmeans1.m)
  """

  return _Runtime.call("spm_kmeans1", *args, **kwargs)
