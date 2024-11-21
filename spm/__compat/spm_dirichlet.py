from spm.__wrapper__ import Runtime


def spm_dirichlet(*args, **kwargs):
    """
      Dirichlet distribution - deprecated  
          
        FORMAT [p] = dirichlet(x,alpha)  
          
        x     - vector of outcome/event probabilities  
        alpha - vector of observed events  
       __________________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
          
        Will Penny  
        $Id: spm_dirichlet.m 4418 2011-08-03 12:00:13Z guillaume $  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_dirichlet.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dirichlet", *args, **kwargs)
