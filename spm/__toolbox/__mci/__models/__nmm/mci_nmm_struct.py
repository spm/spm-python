from spm.__wrapper__ import Runtime


def mci_nmm_struct(*args, **kwargs):
    """
      Set up two region NMM   
        FORMAT [M,U] = mci_nmm_struct (back,sd,Np)  
         
        back      1 to include backward connection (default)  
        sd        Observation noise SD (default 0.01)  
        Np        number of params (2,6 or 21)  
         
        M         Model structure  
        U         Inputs  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_nmm_struct", *args, **kwargs)
