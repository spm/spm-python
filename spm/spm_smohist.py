from spm.__wrapper__ import Runtime


def spm_smohist(*args, **kwargs):
    """
      Smooth a histogram  
        FORMAT [sig,alpha] = spm_smohist(t,lam)  
        t     - a column vector, or matrix of column vectors containing  
                histogram data.  
        lam   - regularisation parameter, or vector of regularisation  
                parameters for each column of t.  
        sig   - smoothed probability density function(s)  
                (columns sum to 1).  
        alpha - logarithm of sig.  
       __________________________________________________________________________  
         
        Maximises: -sum(log(sig).*t) + 0.5*a'*G*a  
        where: sig = exp(a)/sum(exp(a))  
          and: G = lam*L'*L - where L is the Laplacian operator.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_smohist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_smohist", *args, **kwargs)
