from spm.__wrapper__ import Runtime


def _read_besa_tfc(*args, **kwargs):
    """
      READ_BESA_TFC imports data from a BESA *.tfc file  
         
        Use as  
          [DataType, ConditionName, Channels, Time, Frequency, Data] = read_besa_tfc(FILENAME)  
         
        This reads data from the BESA Time-Frequency-Coherence output data file  
        FILENAME and returns the following data:  
          ConditionName: name of analyzed condition  
          ChannelLabels: character array of channel labels  
          Time: array of sampled time instants  
          Frequency: array of sampled frequencies  
          Data: 3D data matrix with indices (channel,time,frequency)  
          Info: Struct containing additional information:  
              DataType: type of the exported data  
              ConditionName: name of analyzed condition  
              NumbeOfTrials: Number of trials on which the data is based  
              StatisticsCorrection: Type of statistics correction for multiple testing  
              EvokedSignalSubtraction: Type of evoked signal subtraction  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_besa_tfc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_besa_tfc", *args, **kwargs)
