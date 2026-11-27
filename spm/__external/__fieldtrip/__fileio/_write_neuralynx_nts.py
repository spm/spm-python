from spm._runtime import Runtime


def _write_neuralynx_nts(*args, **kwargs):
    r"""
      WRITE_NEURALYNX_NTS writes spike timestamps to a NTS file  
         
        Use as  
          write_neuralynx_nts(filename, nts)  
         
        See also READ_NEURALYNX_NTS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_neuralynx_nts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_neuralynx_nts", *args, **kwargs, nargout=0)
