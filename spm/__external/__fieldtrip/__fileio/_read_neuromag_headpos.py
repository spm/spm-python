from spm._runtime import Runtime


def _read_neuromag_headpos(*args, **kwargs):
    r"""
      READ_NEUROMAG_HEADPOS reads head position information from file. The file  
        contains information about Time, Quaternions (q1-q6), goodness of  
        fit (g-value) and error.  
        Time       q1       q2       q3       q4       q5       q6       g-value  error      
         
        data = read_neuromag_headpos(filename)  
         
        where the returned structure data has the fields  
          data.data      Contains the numeric values  
          data.textdata  Contains the Column name  
          data.coldata   Contains the Column name  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neuromag_headpos.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neuromag_headpos", *args, **kwargs)
