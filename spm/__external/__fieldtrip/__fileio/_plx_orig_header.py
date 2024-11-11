from spm.__wrapper__ import Runtime


def _plx_orig_header(*args, **kwargs):
    """
      PLX_ORIG_HEADER Extracts the header informations of plx files using the  
        Plexon Offline SDK, which is available from  
        http://www.plexon.com/assets/downloads/sdk/ReadingPLXandDDTfilesinMatlab-mexw.zip  
         
        Use as  
          [orig] = plx_orig_header(filename)  
         
        Copyright (C) 2012 by Thomas Hartmann  
         
        This code can be redistributed under the terms of the GPL version 3 or  
        newer.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/plx_orig_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("plx_orig_header", *args, **kwargs)
