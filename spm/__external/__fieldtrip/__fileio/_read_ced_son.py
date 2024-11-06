from spm.__wrapper__ import Runtime


def _read_ced_son(*args, **kwargs):
    """
      READ_CED_SON  
         
        [OUT] = read_ced_son(DATAFILE,VARARGIN);  
         
        Reads a analog and event data from a CED SON file   
        (SON files are created by Spike2 software). Currently, only   
        analog channels and event data can be read.   
         
        Optional parameter      Default  
          'readevents'          'no'  
          'readdata'            'no'  
          'readtimestamps'      'no'  
          'begsample'           -1  
          'endsample'           -1  
          'channels'             []        
          
        Please note that CED DAQ systems do a sequential ADC, thus   
        channels do not share the same time axis: The timestamps of the  
        analog channels differ on a subsample level. Use the 'readtimestamps'  
        input parameter to get a matrix with time axes corresponding  
        to the data channels.  
         
        Use begsample and endsample parameters to specify the boundaries  
        of the requested data chunk. Setting these parameters to -1 will  
        return data from the start or until the end of the datafile,  
        respectively.  
         
        Specifying [1,2] for 'channels' will load the 1st and the 2nd   
        analog channel, __regardless of the actual channel number__  
        If, for example channel 1,2,3 are event channels, 4 as an analog  
        channel, 5 is an event channel, and 6 is and analog channel,   
        specifying [1 2] for 'channels' will load analog channel 4 and 6.  
        Specifying [] for channels will return all analog channels.  
         
        Setting 'readtimestamps' to 'yes' will return a time vector for  
        each analog channel.  
         
        Depending on the input parameters, the function will return a structure   
        with fields:   
           'header'       Header information of the SON file  
           'event'        All data from event channels are pooled   
                          and stored in this structure.  
           'data'         Cell-array with analog data  
           'time'         Cell-array with time vectors corresponding to 'data'  
         
        Uses Neuroshare libraries to read Spike2 SON data   
        (see: http://neuroshare.sourceforge.net)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ced_son.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ced_son", *args, **kwargs)
