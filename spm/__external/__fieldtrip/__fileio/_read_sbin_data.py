from spm.__wrapper__ import Runtime


def _read_sbin_data(*args, **kwargs):
    """
      READ_SBIN_DATA reads the data from an EGI segmented simple binary format file  
         
        Use as  
          [trialData] = read_sbin_data(filename, hdr, begtrial, endtrial, chanindx)  
        with  
          filename       name of the input file  
          hdr            header structure, see FT_READ_HEADER  
          begtrial       first trial to read, mutually exclusive with begsample+endsample  
          endtrial       last trial to read,  mutually exclusive with begsample+endsample  
          chanindx       list with channel indices to read  
         
        This function returns a 3-D matrix of size Nchans*Nsamples*Ntrials.  
       _______________________________________________________________________  
         
         
        Modified from EGI's readEGLY.m with permission 2008-03-31 Joseph Dien  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_sbin_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_sbin_data", *args, **kwargs)
