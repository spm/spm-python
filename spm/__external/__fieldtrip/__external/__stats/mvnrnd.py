from spm.__wrapper__ import Runtime


def mvnrnd(*args, **kwargs):
    """
     MVNRND Random vectors from the multivariate normal distribution. This is an   
          open source version that emulates a subpart of the behavior of the same  
          name function from the MATLAB stats-toolbox.  
          It emulates the 3 input, 1 output argument MATLAB-version,   
          where the 3 input argument is the number of samples. If  
          more than three input arguments are provided, an error is thrown. Also,  
          the input argument SIGMA cannot be 3D.  
         
          R = MVNRND(MU,SIGMA) returns an N-by-D matrix R of random vectors  
          chosen from the multivariate normal distribution with mean vector MU,  
          and covariance matrix SIGMA.  MU is an N-by-D matrix, and MVNRND  
          generates each row of R using the corresponding row of MU.  SIGMA is a  
          D-by-D symmetric positive semi-definite matrix.  
          If the covariance matrix is diagonal, containing  
          variances along the diagonal and zero covariances off the diagonal,  
          SIGMA may also be specified as a 1-by-D matrix,  
          containing just the diagonal. If MU is a 1-by-D vector, MVNRND  
          replicates it to match the trailing dimension of SIGMA.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/mvnrnd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mvnrnd", *args, **kwargs)
