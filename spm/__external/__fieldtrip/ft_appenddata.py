from spm.__wrapper__ import Runtime


def ft_appenddata(*args, **kwargs):
    """
      FT_APPENDDATA concatenates multiple raw data structures that have been preprocessed  
        separately into a single raw data structure.  
         
        Use as  
          data = ft_appenddata(cfg, data1, data2, data3, ...)  
         
        The following configuration options are supported:  
          cfg.keepsampleinfo  = 'yes', 'no', 'ifmakessense' (default = 'ifmakessense')  
         
        If the input datasets all have the same channels, the trials will be concatenated.  
        This is useful for example if you have different experimental conditions, which,  
        besides analyzing them separately, for some reason you also want to analyze  
        together. The function will check for consistency in the order of the channels. If  
        the order is inconsistent the channel order of the output will be according to the  
        channel order of the first data structure in the input.  
         
        If the input datasets have different channels, but the same number of trials, the  
        channels will be concatenated within each trial. This is useful for example if the  
        data that you want to analyze contains both MEG and EMG channels which require  
        different preprocessing options.  
         
        If you concatenate trials and the data originates from the same original datafile,  
        the sampleinfo is consistent and you can specify cfg.keepsampleinfo='yes'. If the  
        data originates from different datafiles, the sampleinfo is inconsistent and does  
        not point to the same recording, hence you should specify cfg.keepsampleinfo='no'.  
         
        Occasionally, the data needs to be concatenated in the trial dimension while  
        there's a slight discrepancy in the channels in the input data (e.g. missing  
        channels in one of the data structures). The function will then return a data  
        structure containing only the channels which are present in all inputs.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure. The data structure in the input file should be a  
        cell-array for this particular function.  
         
        See also FT_PREPROCESSING, FT_DATAYPE_RAW, FT_APPENDTIMELOCK, FT_APPENDFREQ,  
        FT_APPENDSOURCE, FT_APPENDSENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_appenddata.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_appenddata", *args, **kwargs)
