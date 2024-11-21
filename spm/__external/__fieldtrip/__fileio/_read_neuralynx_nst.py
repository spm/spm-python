from spm.__wrapper__ import Runtime


def _read_neuralynx_nst(*args, **kwargs):
    """
      READ_NEURALYNX_NST reads a single stereotrode file  
         
        Use as  
          [nst] = read_neuralynx_nst(filename)  
          [nst] = read_neuralynx_nst(filename, begrecord, endrecord)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_nst.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_nst", *args, **kwargs)
