from spm.__wrapper__ import Runtime


def spm_phi_dot(*args, **kwargs):
    """
      Return the derivative of the logistic function  
        FORMAT [y] = spm_phi_dot(x)  
        see spm_phi and spm_inv_phi  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_phi_dot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_phi_dot", *args, **kwargs)
