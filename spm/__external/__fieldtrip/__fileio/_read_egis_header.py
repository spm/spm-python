from spm._runtime import Runtime


def _read_egis_header(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_egis_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_egis_header", *args, **kwargs)
