from spm._runtime import Runtime


def _read_neuralynx_nse(*args, **kwargs):
    r"""
      READ_NEURALYNX_NSE reads a single electrode waveform file  
         
        Use as  
          [nse] = read_neuralynx_nse(filename)  
          [nse] = read_neuralynx_nse(filename, begrecord, endrecord)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neuralynx_nse.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neuralynx_nse", *args, **kwargs)
