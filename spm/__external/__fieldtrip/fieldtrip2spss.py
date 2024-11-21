from spm.__wrapper__ import Runtime


def fieldtrip2spss(*args, **kwargs):
    """
      FIELDTRIP2SPSS compiles data and correpsonding labels into a textfile,  
        suitable for importing into SPSS or JASP (jasp-stats.org).  
         
        Use as  
          fieldtrip2spss(filename, labels, data)  
         
        When exporting from MATLAB, set:  
          - filename; should be string (e.g. 'counts.txt')  
          - labels; should be a cell-array (e.g. {'ones', 'twos', 'threes'})  
          - data; should be either a vector or matrix (e.g. [1 2 3; 1 2 3; 1 2 3])  
         
        When importing to SPSS, set;  
          - variables included at top of file: 'yes'  
          - first case of data on line number: '2' (default)  
          - delimiter appearing between variables: 'tab' (default)  
         
        In case the columns that make up the data matrix have unequal lengths  
        (e.g. because of different number of subjects per group), use:  
          data         = ones(30,2)*9999  
          data(1:30,1) = 1 (30 subj in Group 1)  
          data(1:20,2) = 2 (20 subj in Group 2)  
        After importing to SPSS, click the Missing cell in the Variable View  
        window and enter 9999 as the missing value definition.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fieldtrip2spss.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fieldtrip2spss", *args, **kwargs, nargout=0)
