from spm.__wrapper__ import Runtime


def spm_mci_flow_sun(*args, **kwargs):
    """
      Evaluate flow for Sundials routines  
        FORMAT [f, flag, new_data] = spm_mci_flow_sun (t, x, data)  
         
        t     time  
        x     state  
        data  .U inputs, .P parameters, .M model  
         
        f     flow, dx/dt  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_flow_sun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_flow_sun", *args, **kwargs)
