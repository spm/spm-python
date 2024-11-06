from spm.__wrapper__ import Runtime


def mci_lds_plot_params(*args, **kwargs):
    """
      Plot results of group LDS estimation  
        FORMAT [rmse] = mci_lds_plot_results (MCI,lds)  
         
        MCI      MCI-MFX data structure  
        lds      true model data structure with fields:  
         
        .pinit    true init params  
        .pflow    true flow params  
         
        rmse      root mean square errors  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_plot_params.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_lds_plot_results", *args, **kwargs)
