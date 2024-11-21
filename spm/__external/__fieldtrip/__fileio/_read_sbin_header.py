from spm.__wrapper__ import Runtime


def _read_sbin_header(*args, **kwargs):
    """
      READ_SBIN_HEADER reads the header information from an EGI segmented simple binary format file  
         
        Use as  
          [header_array, CateNames, CatLengths, preBaseline] = read_sbin_header(filename)  
        with  
          header_array     - differs between versions, read code for details  
          CateNames        - category names  
          CatLengths       - length of category names  
          preBaseline      - number of samples in the baseline prior to the baseline event  
        and  
          filename    - the name of the data file  
         
        Since there is no unique event code for the segmentation event, and hence the baseline period,  
        the first event code in the list will be assumed to be the segmentation event.  
        NetStation itself simply ignores possible baseline information when importing simple binary files.  
       _______________________________________________________________________  
         
         
        Modified from EGI's readEGLY.m with permission 2008-03-31 Joseph Dien  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_sbin_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_sbin_header", *args, **kwargs)
