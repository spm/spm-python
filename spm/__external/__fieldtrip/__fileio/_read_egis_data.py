from spm.__wrapper__ import Runtime


def _read_egis_data(*args, **kwargs):
    """
      READ_EGIS_DATA reads the data from an EGI EGIS format file  
         
        Use as  
          dat = read_egis_data(filename, hdr, begtrial, endtrial, chanindx);  
        where  
          filename       name of the input file  
          hdr            header structure, see FT_READ_HEADER  
          begtrial       first trial to read, mutually exclusive with begsample+endsample  
          endtrial       last trial to read,  mutually exclusive with begsample+endsample  
          chanindx       list with channel indices to read  
         
        This function returns a 3-D matrix of size Nchans*Nsamples*Ntrials.  
        Note that EGIS session files are defined as always being epoched.  
        For session files the trials are organized with the members of each cell grouped  
        together.  For average files the "trials" (subjects) are organized with the cells  
        also grouped together (e.g., "cell1sub1, cell1sub2, ...).  
       _______________________________________________________________________  
         
         
        Modified from EGI's EGI Toolbox with permission 2007-06-28 Joseph Dien  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_egis_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_egis_data", *args, **kwargs)
