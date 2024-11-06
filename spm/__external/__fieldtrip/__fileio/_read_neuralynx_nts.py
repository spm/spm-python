from spm.__wrapper__ import Runtime


def _read_neuralynx_nts(*args, **kwargs):
    """
      READ_NEURALYNX_NTS reads spike timestamps  
         
        Use as  
          [nts] = read_neuralynx_nts(filename)  
          [nts] = read_neuralynx_nts(filename, begrecord, endrecord)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_nts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_nts", *args, **kwargs)
