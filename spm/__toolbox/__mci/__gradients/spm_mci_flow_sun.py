from spm._runtime import Runtime


def spm_mci_flow_sun(*args, **kwargs):
    r"""
      Evaluate flow for Sundials routines  
        FORMAT [f, flag, new_data] = spm_mci_flow_sun (t, x, data)  
         
        t     time  
        x     state  
        data  .U inputs, .P parameters, .M model  
         
        f     flow, dx/dt  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/gradients/spm_mci_flow_sun.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_flow_sun", *args, **kwargs)
