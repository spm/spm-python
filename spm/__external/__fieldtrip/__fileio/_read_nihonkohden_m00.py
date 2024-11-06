from spm.__wrapper__ import Runtime


def _read_nihonkohden_m00(*args, **kwargs):
    """
      READ_NIHONKOHDEN_M00 reads the header and data from a file in the Nihon Kohden *.m00 format.  
        This implementation is an adaptation of convert_nkascii2mat.m and get_nkheader.m written  
        by Timothy Ellmore, see https://openwetware.org/wiki/Beauchamp:AnalyzeEEGinMatlab.  
         
        Use as  
          [hdr, dat] = read_nihonkohden_m00(filename)  
         
        This returns a FieldTrip compatible header structure and the data matrix.  
         
        See also FT_READ_HEADER, FT_READ_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nihonkohden_m00.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nihonkohden_m00", *args, **kwargs)
