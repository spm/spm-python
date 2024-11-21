from spm.__wrapper__ import Runtime


def _read_tmsi_poly5(*args, **kwargs):
    """
      READ_TMSI_POLY5  
         
        Use as  
          hdr = read_tmri_poly5(filename)  
          dat = read_tmsi_poly5(filename, hdr, begblock, endblock)  
         
        This implementation is as closely as possible based on the original "tms_read",  
        which contains the comments  
         
          Changed on 08-10-2014 by TL, TMSi  
          - Now supports loading a file from different directory than the script file  
          - Feedback on the validity of arguments and whether a file could be found or not.  
          - Dialogue is opened when no argument was given.  
         
          Changed on 18-10-2022 by JMS, DCCN  
          - Massive speed up: no intermediate double->single->double conversion ,and  
          - Don't store metadata that is not broadcasted to outside function in a struct array, and  
          - Allow for a selection of channels to be read, reducing memory footprint, and calibration step  
         
        This program is distributed in the hope that it will be useful,  
        but WITHOUT ANY WARRANTY; without even the implied warranty of  
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tmsi_poly5.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_tmsi_poly5", *args, **kwargs)
