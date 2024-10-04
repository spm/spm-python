from spm.__wrap__ import _Runtime


def fieldtrip2homer(*args, **kwargs):
  """  FIELDTRIP2HOMER converts a continuous raw data structure from FieldTrip format to  
    Homer format.  
     
    Use as  
      nirs = fieldtrip2homer(data, ...)  
    where the input data structure is formatted according to the output of  
    FT_PREPROCESSING and the output nirs structure is according to Homer.  
     
    Additional options should be specified in key-value pairs and can be  
      'event'        = event structure that corresponds to the data, see FT_READ_EVENT  
     
    See https://www.nitrc.org/plugins/mwiki/index.php/homer2:Homer_Input_Files#NIRS_data_file_format  
    for a description of the Homer data structure.  
     
    See also HOMER2FIELDTRIP, FT_PREPROCESSING, FT_DATATYPE_RAW  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fieldtrip2homer.m)
  """

  return _Runtime.call("fieldtrip2homer", *args, **kwargs)
