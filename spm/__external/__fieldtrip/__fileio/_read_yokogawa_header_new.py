from spm._runtime import Runtime


def _read_yokogawa_header_new(*args, **kwargs):
    """
      READ_YOKOGAWA_HEADER_NEW reads the header information from continuous,  
        epoched or averaged MEG data that has been generated by the Yokogawa  
        MEG system and software and allows that data to be used in combination  
        with FieldTrip.  
         
        Use as  
         [hdr] = read_yokogawa_header_new(filename)  
         
        This is a wrapper function around the functions  
        getYkgwHdrSystem  
        getYkgwHdrChannel  
        getYkgwHdrAcqCond  
        getYkgwHdrCoregist  
        getYkgwHdrDigitize  
        getYkgwHdrSource  
         
        See also CTF2GRAD, BTI2GRAD, FIF2GRAD, MNE2GRAD, ITAB2GRAD, FT_READ_SENS,  
        FT_READ_HEADER, READ_YOKOGAWA_DATA_NEW, READ_YOKOGAWA_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_yokogawa_header_new.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_yokogawa_header_new", *args, **kwargs)
