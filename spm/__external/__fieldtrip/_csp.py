from spm.__wrapper__ import Runtime


def _csp(*args, **kwargs):
    """
      CSP calculates the common spatial pattern (CSP) projection.  
         
        Use as:  
          [W] = csp(C1, C2, m)  
         
        This function implements the intents of the CSP algorithm described in [1].  
        Specifically, CSP finds m spatial projections that maximize the variance (or  
        band power) in one condition (described by the [p x p] channel-covariance  
        matrix C1), and simultaneously minimizes the variance in the other (C2):  
         
          W C1 W' = D  
         
        and  
         
          W (C1 + C2) W' = I,  
         
        Where D is a diagonal matrix with decreasing values on it's diagonal, and I  
        is the identity matrix of matching shape.  
        The resulting [m x p] matrix can be used to project a zero-centered [p x n]  
        trial matrix X:  
         
          S = W X.  
         
         
        Although the CSP is the de facto standard method for feature extraction for  
        motor imagery induced event-related desynchronization, it is not strictly  
        necessary [2].  
         
        [1] Zoltan J. Koles. The quantitative extraction and topographic mapping of  
            the abnormal components in the clinical EEG. Electroencephalography and  
            Clinical Neurophysiology, 79(6):440--447, December 1991.  
         
        [2] Jason Farquhar. A linear feature space for simultaneous learning of  
            spatio-spectral filters in BCI. Neural Networks, 22:1278--1285, 2009.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/csp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("csp", *args, **kwargs)
