from spm.__wrapper__ import Runtime


def DEM_Stephen(*args, **kwargs):
    """
      FORMAT Tab = DEM_Stephen  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        This routine evaluates outcomes under some intervention over a specified  
        set of dates. The outcomes are then tabulated and displayed in the MATLAB  
        window. specify the duration and (parametric) nature of the intervention  
        by editing the code below; namely, the non-pharmacological intervention  
        structure NPI.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_Stephen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_Stephen", *args, **kwargs)
