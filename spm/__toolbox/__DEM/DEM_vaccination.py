from spm._runtime import Runtime


def DEM_vaccination(*args, **kwargs):
    """
      FORMAT Tab = DEM_vaccination  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        This routine evaluates outcomes under some intervention over a specified  
        set of dates. The outcomes are then tabulated and displayed in the MATLAB  
        window. specify the duration and (parametric) nature of the intervention  
        by editing the code below; namely, the non-pharmacological intervention  
        structure NPI.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_vaccination.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_vaccination", *args, **kwargs)
