from spm.__wrapper__ import Runtime


def _read_mayo_mef21(*args, **kwargs):
    """
      READ_MAYO_MEF21 read header, event and data from the files formatted in MEF2.1  
         
        Syntax:  
          hdr = read_mayo_mef21(filename)  
          hdr = read_mayo_mef21(filename, password)  
          evt = read_mayo_mef21(filename, password, hdr)  
          dat = read_mayo_mef21(filename, password, hdr, begsample, endsample, chanindx)  
         
        Input(s):  
          filename        - [char] name of the file or folder of the dataset  
          password        - [struct] (opt) password structure of MEF 2.1 data (see  
                            MEFSession_2.1)  
          hdr             - [struct] (opt) header structure of the dataset (see  
                            ft_read_header; default = struct([]))  
          begsample       - [num] (opt) first sample to read (default = [])  
          endsample       - [num] (opt) last smaple to read (default = [])  
          chanindx        - [num] (opt) list of channel indices to read (default  
                            = [])  
         
        Output(s):  
          hdr             - [struct] header structure of the dataset (see   
                            FT_READ_HEADER)  
          evt             - [struct] event structure of the dataset (see  
                            FT_READ_EVENT)  
          dat             - [num] data read in  
         
        Example:  
         
        Note:  
         
        References:  
         
        See also ft_filetype, ft_read_header, ft_read_event, ft_read_data.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mayo_mef21.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_mayo_mef21", *args, **kwargs)
