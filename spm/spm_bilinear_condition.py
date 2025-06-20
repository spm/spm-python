from spm._runtime import Runtime


def spm_bilinear_condition(*args, **kwargs):
    """
      Condition a bilinear operator by suppressing positive eigenmodes  
        FORMAT M0 = spm_bilinear_condition(M0)  
        M0 - bilinear operator  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bilinear_condition.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bilinear_condition", *args, **kwargs)
