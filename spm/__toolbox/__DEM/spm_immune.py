from spm._runtime import Runtime


def spm_immune(*args, **kwargs):
    r"""
      Variational inversion of immune model  
        FORMAT [F,Ep,Cp,pE,pC,Eh] = spm_immune(Y,U,pE,pC,hC)  
        Y   - timeseries data  
        pE  - prior expectation of parameters  
        pC  - prior covariances of parameters  
        hC  - prior covariances of precisions  
          
        F   - log evidence (negative variational free energy)  
        Ep  - posterior expectation of parameters  
        Cp  - posterior covariances of parameters  
        pE  - prior expectation of parameters  
        pC  - prior covariances of parameters  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_immune.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_immune", *args, **kwargs)
