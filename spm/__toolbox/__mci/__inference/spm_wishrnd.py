from spm.__wrapper__ import Runtime


def spm_wishrnd(*args, **kwargs):
    """
      Generate N samples from Wishart density  
        FORMAT [S] = spm_wishrnd (B,a,N)  
         
        B,a   Wishart params, d=dim(B)  
        N     Number of samples  
        S     [d x d x N] sample matrices or [d x d] if N=1  
         
        The Wishart density here, W(S;a,B), is defined as in p. 435 of  
        J. Bernardo and A. Smith, Bayesian Theory, Wiley, 2000.   
        We have E[S]=aB^{-1}  
          
        This definition is different to eg. C. Bishop,   
        Pattern Recognition and Machine Learning, Springer, 2006., who  
        have W(S;n,V). They are related by n=2a, V=B^{-1}/2. We have E[S]=nV  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_wishrnd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_wishrnd", *args, **kwargs)
