from spm.__wrapper__ import Runtime


def _read_egis_header(*args, **kwargs):
    """
      READ_EGIS_HEADER reads the header information from an EGI EGIS format file  
         
        Use as  
          [fhdr chdr] = read_egia_header(filename)  
        with  
          fhdr        - the file header information  
          chdr        - the cell header information  
          ename       - experiment name  
          cnames      - cell names  
          fcom        - comments  
          ftext       - general text  
        and  
          filename    - the name of the data file  
       _______________________________________________________________________  
         
         
        Modified from EGI's EGI Toolbox with permission 2007-06-28 Joseph Dien  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_egis_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_egis_header", *args, **kwargs)
