from spm._runtime import Runtime


def _read_bdf(*args, **kwargs):
    r"""
      READ_BDF Read EEG data from a Biosemi BDF file  
         
          [data, header] = read_bdf(filename)  
          [data, header] = read_bdf(filename, 'Param', value, ...)  
         
        Inputs:  
          filename - BDF filename (including .bdf extension)  
         
        Outputs:  
          data    - EEG data matrix (Nchannels × Ntimepoints)  
          header  - Structure containing header information  
         
        Optional parameters:  
          'Channels'    - Cell array of channel names to read (default: all)  
          'TimeRange'   - [start end] in seconds (default: all)  
          'Verbose'     - Display progress info (default: true)  
         
        Example:  
          [eeg, hdr] = read_bdf('eeg_data.bdf');  
          [eeg, hdr] = read_bdf('eeg_data.bdf', 'Channels', {'Fz', 'Cz', 'Pz'}, 'TimeRange', [10 20]);  
         
        See also WRITE_BDF  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_bdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_bdf", *args, **kwargs)
