from spm.__wrapper__ import Runtime


def _read_neuralynx_ntt(*args, **kwargs):
    """
      READ_NEURALYNX_NTT reads a single tetrode file  
         
        Use as  
          [ntt] = read_neuralynx_ntt(filename)  
          [ntt] = read_neuralynx_ntt(filename, begrecord, endrecord)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_ntt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_ntt", *args, **kwargs)
