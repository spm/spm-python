from spm.__wrapper__ import Runtime


def _read_dhn_med10(*args, **kwargs):
    """
      READ_DHN_MED10 read header, event, and waveform data formated in Dark Horse Neuron MED 1.0  
         
        Syntax:  
          hdr = read_dhn_med10(filename)  
          hdr = read_dhn_med10(filename, password)  
          hdr = read_dhn_med10(filename, password, sortchannel)  
          evt = read_dhn_med10(filename, password, sortchannel, hdr)  
          dat = read_dhn_med10(filename, password, sortchannel, hdr, begsample, endsample, chanindx)  
         
        Input(s):  
          filename        - [char] name of the file or folder of the dataset  
          password        - [struct] (opt) password structure of MED 1.0 data (see  
                            MEDSession_1p0)  
          sortchannel     - [char] (opt) sort channel order either alphabetically  
                            'alphabet' or numerically 'number' (default = 'alphabet')  
          hdr             - [struct] (opt) header structure of the dataset (see FT_READ_HEADER; default = struct([]))  
          begsample       - [num] (opt) first sample to read (default = [])  
          endsample       - [num] (opt) last smaple to read (default = [])  
          chanindx        - [num] (opt) list of channel indices to read (default = [])  
         
        Output(s):  
          hdr             - [struct] header structure of the dataset (see FT_READ_HEADER)  
          evt             - [struct] event structure of the dataset (see FT_READ_EVENT)  
          dat             - [num] data read in  
         
        Example:  
         
        Note:  
         
        References:  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_EVENT, FT_READ_DATA.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_dhn_med10.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_dhn_med10", *args, **kwargs)
