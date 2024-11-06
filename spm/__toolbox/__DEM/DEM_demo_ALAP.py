from spm.__wrapper__ import Runtime


def DEM_demo_ALAP(*args, **kwargs):
    """
      This demonstration is essentially the same as DEM_demo_LAP - however  
        here, we compare two generalised filtering schemes that are implemented  
        very differently: the first integrates the generative process in  
        parallel with the inversion, while the standard spm_LAP scheme inverts a  
        model given pre-generated data. The advantage of generating and modelling  
        data  contemporaneously is that it allows the inversion scheme to couple  
        back to the generative process through action (see active inference  
        schemes): spm_ALAP.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_ALAP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_ALAP", *args, **kwargs, nargout=0)
