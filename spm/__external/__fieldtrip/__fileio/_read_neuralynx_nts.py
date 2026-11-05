from spm._runtime import Runtime


def _read_neuralynx_nts(*args, **kwargs):
    r"""
      READ_NEURALYNX_NTS reads spike timestamps  
         
        Use as  
          [nts] = read_neuralynx_nts(filename)  
          [nts] = read_neuralynx_nts(filename, begrecord, endrecord)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neuralynx_nts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neuralynx_nts", *args, **kwargs)
