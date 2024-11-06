from spm.__wrapper__ import Runtime


def spm_mci_vw_init(*args, **kwargs):
    """
      Initialise fixed and random effects  
        FORMAT [w_init,v_init,assign,update_ffx,update_rfx] = spm_mci_vw_init (MCI)  
         
        MCI       MCI data structure  
         
        w_init        initial rfx values  
        v_init        initial ffx values  
        assign        data structure describing how rfx/ffx are assigned   
                      to initial conditions, flow and output params  
        update_ffx    (1/0)  
        update_rfx    (1/0)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_vw_init.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_vw_init", *args, **kwargs)
