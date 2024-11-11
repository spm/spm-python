from spm.__wrapper__ import Runtime


def _write_gdf(*args, **kwargs):
    """
      WRITE_GDF(filename, header, data)  
         
        Writes a GDF file from the given header (only label, Fs, nChans are of interest)  
        and the data (unmodified). Digital and physical limits are derived from the data  
        via min and max operators. The GDF file will contain N records of 1 sample each,  
        where N is the number of columns in 'data'.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_gdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_gdf", *args, **kwargs, nargout=0)
