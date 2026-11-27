from spm._runtime import Runtime


def fiff_read_hpi_result(*args, **kwargs):
    r"""
       
        [ res ] = fiff_read_hpi_result(name)  
         
        Read the HPI result block from a measurement file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_hpi_result.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_hpi_result", *args, **kwargs)
