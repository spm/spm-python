from spm.__wrapper__ import Runtime


def spm_mar_gen(*args, **kwargs):
    """
      Generate data from MAR model  
        FORMAT [v] = spm_mar_gen (w,A,C,n,ndisc)  
         
        Generates n time steps of the MAR(p) process  
         
            v(k,:)' = w' + A1*v(k-1,:)' +...+ Ap*v(k-p,:)' + eta(k,:)',   
         
         where A=[A1 ... Ap] is the coefficient matrix, and w is a vector of  
         intercept terms that is included to allow for a nonzero mean of the  
         process. The vectors eta(k,:) are independent Gaussian noise  
         vectors with mean zero and covariance matrix C.  
         
         This function is adapted from the ARFIT toolbox by Neumaier and  
         Schneider  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mar_gen", *args, **kwargs)
