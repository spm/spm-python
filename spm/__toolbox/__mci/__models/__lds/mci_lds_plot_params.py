from spm._runtime import Runtime


def mci_lds_plot_params(*args, **kwargs):
    r"""
      Plot results of group LDS estimation  
        FORMAT [rmse] = mci_lds_plot_results (MCI,lds)  
         
        MCI      MCI-MFX data structure  
        lds      true model data structure with fields:  
         
        .pinit    true init params  
        .pflow    true flow params  
         
        rmse      root mean square errors  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/lds/mci_lds_plot_params.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_lds_plot_results", *args, **kwargs)
