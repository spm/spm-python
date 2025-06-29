from spm._runtime import Runtime


def _neuralynx_crc(*args, **kwargs):
    """
      NEURALYNX_CRC computes a cyclic redundancy check  
         
        Use as  
          crc = neuralynx_crc(dat)  
         
        Note that the CRC is computed along the first dimension.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/neuralynx_crc.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("neuralynx_crc", *args, **kwargs)
