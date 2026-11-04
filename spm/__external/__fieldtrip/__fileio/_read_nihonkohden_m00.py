from spm._runtime import Runtime


def _read_nihonkohden_m00(*args, **kwargs):
    r"""
      READ_NIHONKOHDEN_M00 reads the header and data from a file in the Nihon Kohden *.m00 format.  
        This implementation is an adaptation of convert_nkascii2mat.m and get_nkheader.m written  
        by Timothy Ellmore, see https://openwetware.org/wiki/Beauchamp:AnalyzeEEGinMatlab.  
         
        Use as  
          [hdr, dat] = read_nihonkohden_m00(filename)  
         
        This returns a FieldTrip compatible header structure and the data matrix.  
         
        See also FT_READ_HEADER, FT_READ_DATA  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_nihonkohden_m00.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_nihonkohden_m00", *args, **kwargs)
