from spm.__wrapper__ import Runtime


def _read_neuralynx_ncs(*args, **kwargs):
    """
      READ_NEURALYNX_NCS reads a single continuous channel file  
         
        Use as  
          [ncs] = read_neuralynx_ncs(filename)  
          [ncs] = read_neuralynx_ncs(filename, begrecord, endrecord)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_ncs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_ncs", *args, **kwargs)
