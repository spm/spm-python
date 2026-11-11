from spm._runtime import Runtime


def _read_neuralynx_nst(*args, **kwargs):
    r"""
      READ_NEURALYNX_NST reads a single stereotrode file  
         
        Use as  
          [nst] = read_neuralynx_nst(filename)  
          [nst] = read_neuralynx_nst(filename, begrecord, endrecord)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neuralynx_nst.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neuralynx_nst", *args, **kwargs)
