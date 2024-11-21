from spm.__wrapper__ import Runtime


def _read_neuralynx_nse(*args, **kwargs):
    """
      READ_NEURALYNX_NSE reads a single electrode waveform file  
         
        Use as  
          [nse] = read_neuralynx_nse(filename)  
          [nse] = read_neuralynx_nse(filename, begrecord, endrecord)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_nse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_nse", *args, **kwargs)
