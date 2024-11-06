from spm.__wrapper__ import Runtime


def mci_interp_init(*args, **kwargs):
    """
      Linear interpolate to t=0  
        FORMAT [w0] = mci_interp_init (Y,M)  
         
        Y     Cell of data from multiple subjects  
              Y{n}.y, Y{n}.ind for n=1..N  
        M     Model structure  
         
        w0    [d x N] matrix of initial states  
              where d is number of states  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_interp_init.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_interp_init", *args, **kwargs)
