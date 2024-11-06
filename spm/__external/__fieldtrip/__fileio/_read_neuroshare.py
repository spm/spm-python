from spm.__wrapper__ import Runtime


def _read_neuroshare(*args, **kwargs):
    """
      READ_NEUROSHARE reads header information or data from any file format  
        supported by Neuroshare. The file can contain event timestamps, spike  
        timestamps and waveforms, and continuous (analog) variable data.  
         
        Use as:  
          hdr = read_neuroshare(filename, ...)  
          dat = read_neuroshare(filename, ...)  
         
        Optional input arguments should be specified in key-value pairs and may include:  
          'dataformat'    = string  
          'readevent'     = 'yes' or 'no' (default)  
          'readspike'     = 'yes' or 'no' (default)  
          'readanalog'    = 'yes' or 'no' (default)  
          'chanindx'      = list with channel indices to read  
          'begsample      = first sample to read  
          'endsample      = last sample to read  
         
        NEUROSHARE: http://www.neuroshare.org is a site created to support the  
        collaborative development of open library and data file format  
        specifications for neurophysiology and distribute open-source data  
        handling software tools for neuroscientists.  
         
        Note that this is a test version, WINDOWS only  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuroshare.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuroshare", *args, **kwargs)
