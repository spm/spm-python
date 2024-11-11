from spm.__wrapper__ import Runtime


def ft_read_data(*args, **kwargs):
    """
      FT_READ_DATA reads data from a variety of EEG, MEG and other time series data files  
        and represents it in a common data-independent format. The supported formats are  
        listed in the accompanying FT_READ_HEADER function.  
         
        Use as  
          dat = ft_read_data(filename, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          'header'         header structure, see FT_READ_HEADER  
          'begsample'      first sample to read  
          'endsample'      last sample to read  
          'begtrial'       first trial to read, mutually exclusive with begsample+endsample  
          'endtrial'       last trial to read, mutually exclusive with begsample+endsample  
          'chanindx'       list with channel indices to read  
          'chanunit'       cell-array with strings, convert each channel to the desired unit  
          'checkboundary'  boolean, whether to check for reading segments over a trial boundary  
          'checkmaxfilter' boolean, whether to check that maxfilter has been correctly applied (default = true)  
          'cache'          boolean, whether to use caching for multiple reads  
          'dataformat'     string  
          'headerformat'   string  
          'fallback'       can be empty or 'biosig' (default = [])  
          'blocking'       wait for the selected number of events (default = 'no')  
          'timeout'        amount of time in seconds to wait when blocking (default = 5)  
          'password'       password structure for encrypted data set (only for dhn_med10, mayo_mef30 and mayo_mef21)  
         
        This function returns a 2-D matrix of size Nchans*Nsamples for continuous  
        data when begevent and endevent are specified, or a 3-D matrix of size  
        Nchans*Nsamples*Ntrials for epoched or trial-based data when begtrial  
        and endtrial are specified.  
         
        To use an external reading function, you can specify an external function as the  
        'dataformat' option. This function should take five input arguments: filename, hdr,  
        begsample, endsample, chanindx. Please check the code of this function for details,  
        and search for BIDS_TSV as example.  
         
        See also FT_READ_HEADER, FT_READ_EVENT, FT_WRITE_DATA, FT_WRITE_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_data", *args, **kwargs)
