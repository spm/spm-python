from spm.__wrapper__ import Runtime


def _read_bti_hs(*args, **kwargs):
    """
     read_hs_file Reads in BTI-Headshape files  
          filename: file with the headshape informations  
          outfile: if present, a ctf ".shape" file is written  
          output: if present, a 3xN matrix containing the headshape-points  
         
          (C) 2007 by Thomas Hartmann  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bti_hs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_bti_hs", *args, **kwargs)
