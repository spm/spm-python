from spm.__wrapper__ import Runtime


def dcm_fit_finger(*args, **kwargs):
    """
      Fit DCM model to finger data  
        FORMAT [DCM] = dcm_fit_finger(yy,M,U,m)  
         
        yy     -  yy{n} for nth trial data  
        M      -  model structure  
        U      -  input structure  
        m      -  PIF order  
         
        DCM    -  o/p data structure  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/man/example_scripts/dcm_fit_finger.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dcm_fit_finger", *args, **kwargs)
