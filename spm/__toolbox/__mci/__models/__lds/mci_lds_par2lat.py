from spm.__wrapper__ import Runtime


def mci_lds_par2lat(*args, **kwargs):
    """
      Convert parmas to latent params  
        FORMAT [P] = mci_lds_par2lat (Pt,M)  
         
        Pt    params   
        M     model struct  
         
        P     params (latent)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_par2lat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_lds_par2lat", *args, **kwargs)
