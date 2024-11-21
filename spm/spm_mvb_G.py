from spm.__wrapper__ import Runtime


def spm_mvb_G(*args, **kwargs):
    """
      Multivariate Bayesian inversion of a linear model  
        FORMAT model = spm_mvb_G(X,L,X0,G,V);  
        X      - contrast or target vector  
        L      - pattern matrix (n x m)  
        X0     - confounds  
        G      - pattern subsets (in columns of G) (m x h)  
        V      - cell array of observation noise covariance components  
         
        returns model:  
                       F: log-evidence [F(0), F(1),...]  
                       G: pattern switches  
                       h: covariance hyperparameters (on R and cov(E))  
                      qE: conditional expectation of pattern-weights  
                     MAP: MAP projector (pattern-weights)  
                      Cp: prior covariance (pattern space)  
       __________________________________________________________________________  
         
        model: X = L*P + X0*Q + R  
               P = E;             
          cov(E) = h1*diag(G(:,1)) + h2*diag(G(:,2)) + ...  
         
        See spm_mvb and:  
         
        Bayesian decoding of brain images.  
        Friston K, Chu C, Mourão-Miranda J, Hulme O, Rees G, Penny W, Ashburner J.  
        Neuroimage. 2008 Jan 1;39(1):181-205  
          
        Multiple sparse priors for the M/EEG inverse problem.  
        Friston K, Harrison L, Daunizeau J, Kiebel S, Phillips C, Trujillo-Barreto   
        N, Henson R, Flandin G, Mattout J.  
        Neuroimage. 2008 Feb 1;39(3):1104-20.  
          
        Characterizing dynamic brain responses with fMRI: a multivariate approach.  
        Friston KJ, Frith CD, Frackowiak RS, Turner R.  
        Neuroimage. 1995 Jun;2(2):166-72.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_G.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvb_G", *args, **kwargs)
