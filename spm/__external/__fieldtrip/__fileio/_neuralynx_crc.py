from spm._runtime import Runtime


def _neuralynx_crc(*args, **kwargs):
    r"""
      NEURALYNX_CRC computes a cyclic redundancy check  
         
        Use as  
          crc = neuralynx_crc(dat)  
         
        Note that the CRC is computed along the first dimension.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/neuralynx_crc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("neuralynx_crc", *args, **kwargs)
