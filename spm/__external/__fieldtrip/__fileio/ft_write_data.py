from spm.__wrapper__ import Runtime


def ft_write_data(*args, **kwargs):
    """
      FT_WRITE_DATA exports electrophysiological data such as EEG to a file.  
         
        Use as  
          ft_write_data(filename, dat, ...)  
         
        The specified filename can contain the filename extension. If it has no filename  
        extension not, it will be added automatically.  
         
        Additional options should be specified in key-value pairs and can be  
          'header'       = header structure that describes the data, see FT_READ_HEADER  
          'event'        = event structure that corresponds to the data, see FT_READ_EVENT  
          'chanindx'     = 1xN array, for selecting a subset of channels from header and data  
          'dataformat'   = string, see below  
          'append'       = boolean, not supported for all formats  
         
        The supported dataformats for writing are  
          edf  
          gdf  
          anywave_ades  
          brainvision_eeg  
          neuralynx_ncs  
          neuralynx_sdma  
          plexon_nex  
          fcdc_matbin  
          fcdc_mysql  
          fcdc_buffer  
          flac, m4a, mp4, oga, ogg, wav (audio formats)  
          matlab  
          homer_nirs  
          snirf  
         
        For EEG data, the input data is assumed to be scaled in microvolt.  
        For NIRS data, the input data is assumed to represent optical densities.  
         
        See also FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT, FT_WRITE_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_write_data", *args, **kwargs, nargout=0)
