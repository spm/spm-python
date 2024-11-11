from spm.__wrapper__ import Runtime


def _read_neurosim_signals(*args, **kwargs):
    """
      READ_NEUROSIM_SIGNALS reads the "signals" file that is written by Jan  
        van der Eerden's NeuroSim software.  
         
        See also FT_READ_HEADER, FT_READ_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neurosim_signals.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neurosim_signals", *args, **kwargs)
