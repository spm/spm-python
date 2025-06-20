from spm._runtime import Runtime


def fiff_read_hpi_result(*args, **kwargs):
    """
       
        [ res ] = fiff_read_hpi_result(name)  
         
        Read the HPI result block from a measurement file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_hpi_result.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_hpi_result", *args, **kwargs)
