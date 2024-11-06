from spm.__wrapper__ import Runtime


def DATA_WID_data(*args, **kwargs):
    """
      Data retrieval function for COVID modelling  
        FORMAT D = DATA_WID_data  
         
        n   - number of countries to retain [default: n]  
         
        This auxiliary routine retrieves data from comma separated data files  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DATA_WID_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DATA_WID_data", *args, **kwargs)
