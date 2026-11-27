from spm._runtime import Runtime


def spm_dirichlet(*args, **kwargs):
    r"""
      Dirichlet distribution - deprecated  
          
        FORMAT [p] = dirichlet(x,alpha)  
          
        x     - vector of outcome/event probabilities  
        alpha - vector of observed events  
       __________________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
          
        Will Penny  
        $Id: spm_dirichlet.m 4418 2011-08-03 12:00:13Z guillaume $  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/compat/spm_dirichlet.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dirichlet", *args, **kwargs)
