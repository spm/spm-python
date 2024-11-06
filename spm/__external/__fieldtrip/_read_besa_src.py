from spm.__wrapper__ import Runtime


def _read_besa_src(*args, **kwargs):
    """
      READ_BESA_SRC reads a beamformer source reconstruction from a BESA file  
         
        Use as  
          [src] = read_besa_src(filename)  
         
        The output structure contains a minimal representation of the contents  
        of the file.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_besa_src.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_besa_src", *args, **kwargs)
