from spm._runtime import Runtime


def DATA_WID_data(*args, **kwargs):
    r"""
      Data retrieval function for COVID modelling  
        FORMAT D = DATA_WID_data  
         
        n   - number of countries to retain [default: n]  
         
        This auxiliary routine retrieves data from comma separated data files  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DATA_WID_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DATA_WID_data", *args, **kwargs)
