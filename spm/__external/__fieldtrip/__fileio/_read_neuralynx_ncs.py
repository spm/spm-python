from spm._runtime import Runtime


def _read_neuralynx_ncs(*args, **kwargs):
    r"""
      READ_NEURALYNX_NCS reads a single continuous channel file  
         
        Use as  
          [ncs] = read_neuralynx_ncs(filename)  
          [ncs] = read_neuralynx_ncs(filename, begrecord, endrecord)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neuralynx_ncs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neuralynx_ncs", *args, **kwargs)
