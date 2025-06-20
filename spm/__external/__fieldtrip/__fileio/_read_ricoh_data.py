from spm._runtime import Runtime


def _read_ricoh_data(*args, **kwargs):
    """
     function [dat] = read_ricoh_data(filename, hdr, begsample, endsample, chanindx)  
         
        READ_RICOH_DATA reads continuous or averaged MEG data  
        generated by the RICOH MEG system and software,  
        and allows the data to be used in FieldTrip.  
         
        Use as  
          [dat] = read_ricoh_data(filename, hdr, begsample, endsample, chanindx)  
         
        This is a wrapper function around the function getRData  
         
        See also READ_RICOH_HEADER, READ_RICOH_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ricoh_data.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ricoh_data", *args, **kwargs)
