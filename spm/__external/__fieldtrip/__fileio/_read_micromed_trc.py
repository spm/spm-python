from spm.__wrapper__ import Runtime


def _read_micromed_trc(*args, **kwargs):
    """
     --------------------------------------------------------------------------  
        reads Micromed .TRC file into matlab, version Mariska, edited by Romain  
        input: filename  
        output: datamatrix  
       --------------------------------------------------------------------------  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_micromed_trc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_micromed_trc", *args, **kwargs)
