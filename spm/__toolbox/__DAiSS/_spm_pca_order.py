from spm._runtime import Runtime


def _spm_pca_order(*args, **kwargs):
    """
      Model order selection for PCA     
        FORMAT [M_opt,log_ev,lambda,var] = spm_pca_order (X, N)  
         
        Model order selection for PCA using Minka's approximation to model evidence  
        Input can be  
            X         Data  
        or  
             
            X         Covariance matrix  
            N         number of samples used for computing X  
         
        M_opt         Optimum number of sources  
        log_ev        Log Evidence  
        lambda        Eigenspectrum  
        var           Estimated observation noise (at M_opt)  
         
        Algorithm:  
         
        T.P. Minka. Automatic choice of dimensionality for PCA. Technical Report  
        514, MIT Media Lab, Perceptual Computing Section, 2000.  
         
        Evaluation:  
         
        W. Penny, S. Roberts and R. Everson (2000) ICA: model order selection  
        and dynamic source models. ICA: Principles and Practice, pages 299-314.   
        Cambridge University Press.  
       ___________________________________________________________________________  
        Copyright (C) 2008 Wellcome Department of Imaging Neuroscience  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/spm_pca_order.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_pca_order", *args, **kwargs)
