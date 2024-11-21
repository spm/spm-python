from spm.__wrapper__ import Runtime


def mci_logistic_struct(*args, **kwargs):
    """
      Set up data structures for logistic model  
        FORMAT [M,U,Y] = mci_logistic_struct (log_data,T)  
         
        log_data  'pima','ripley' or 'dct'  
        T         for 'dct' we can specify number of samples  
         
        M         model structure  
        U         U.X is the design matrix (independent variables)  
        Y         dependent variable  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/logistic/mci_logistic_struct.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_logistic_struct", *args, **kwargs)
