from spm._runtime import Runtime


def spm_COVID_table(*args, **kwargs):
    r"""
      FORMAT Tab = spm_COVID_table(Ep,Cp,M)  
        FORMAT Tab = spm_COVID_table(DCM)  
        Ep  - conditional expectations  
        Cp  - conditional covariances  
        M   - model  
         
        Tab - table of conditional estimators  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_COVID_table.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_COVID_table", *args, **kwargs)
