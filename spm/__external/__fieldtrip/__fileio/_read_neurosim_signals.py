from spm._runtime import Runtime


def _read_neurosim_signals(*args, **kwargs):
    r"""
      READ_NEUROSIM_SIGNALS reads the "signals" file that is written by Jan  
        van der Eerden's NeuroSim software.  
         
        See also FT_READ_HEADER, FT_READ_DATA  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neurosim_signals.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neurosim_signals", *args, **kwargs)
