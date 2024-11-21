from spm.__wrapper__ import Runtime


def mci_pb_struct(*args, **kwargs):
    """
      Preece-Baines model structure  
        FORMAT [M,U] = mci_pb_struct (Nobs)  
         
        Nobs      Number of observations  
         
        M         Model structure  
        U         Input structure  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/growth/mci_pb_struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_pb_struct", *args, **kwargs)
