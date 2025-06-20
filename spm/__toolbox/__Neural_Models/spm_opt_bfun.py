from spm._runtime import Runtime


def spm_opt_bfun(*args, **kwargs):
    """
       
        FORMAT spm_opt_bfun  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_opt_bfun.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opt_bfun", *args, **kwargs, nargout=0)
