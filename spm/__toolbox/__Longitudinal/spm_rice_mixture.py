from spm.__wrapper__ import Runtime


def spm_rice_mixture(*args, **kwargs):
    """
      Fit a mixture of Ricians to a histogram  
        FORMAT [mg,nu,sig,info] = spm_rice_mixture(h,x,K)  
        h    - histogram counts  
        x    - bin positions (plot(x,h) to see the histogram)  
        K    - number of Ricians  
         
        mg   - integral under each Rician  
        nu   - "mean" parameter of each Rician  
        sig  - "standard deviation" parameter of each Rician  
        info - This struct can be used for plotting the fit as:  
                   plot(info.x(:),info.p,'--',info.x(:), ...  
                        info.h/sum(info.h)/info.md,'b.', ...  
                        info.x(:),info.lse,'r');  
         
        An EM algorithm is used, which involves alternating between computing  
        belonging probabilities, and then the parameters of the Ricians.  
        The Koay inversion technique is used to compute the Rician parameters  
        from the sample means and standard deviations. This is described at  
        https://en.wikipedia.org/wiki/Rician_distribution  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_rice_mixture.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_rice_mixture", *args, **kwargs)
