from spm.__wrapper__ import Runtime


def spm_eeg_merge(*args, **kwargs):
    """
      Concatenate epoched single trial files  
        FORMAT Dout = spm_eeg_merge(S)  
         
        S           - input structure (optional)  
         fields of S:  
          S.D       - character array containing filename of M/EEG mat-files  
                      or cell array of D's  
          S.recode  - this field specifies how the condition labels will be  
                      translated from the original files to the merged file.  
                      Several options are possible:  
                        'same'        - leave the condition labels unchanged  
                        'addfilename' - add the original file name to condition  
                                        label  
                        old way specification - (for backward compatibility)                       
                              a cell array where each cell contains a condition  
                              label. The ordering of these labels must be such   
                              that each row in the cell matrix specifies the   
                              conditionlabels for one of the selected files.  
                        specification via recoding rules - for this S.recode  
                              should be a structure array where each element   
                              specifies a rule using the following fields:  
                                   file - can be a cell array of strings with   
                                          file names, a vector of file indices   
                                          or a string with regular expression   
                                          matching the files to which the rule   
                                          will apply.  
                                   labelorg - can be a cell array of condition   
                                          labels or a string with regular   
                                          expression matching the condition   
                                          labels to which this rule will apply.  
                                   labelnew - new label for the merged file. It  
                                          can contain special tokens #file# and  
                                          #labelorg# that will be replaced by   
                                          the original file name and original   
                                          condition label respectively.  
                              The rule will be applied one after the other so   
                              the last rule takes precedences. Trials not   
                              matched by any of the rules will keep their   
                              original labels.  
                              Example:  
                                 S.recode(1).file     = '.*';  
                                 S.recode(1).labelorg = '.*';  
                                 S.recode(1).labelnew = '#labelorg# #file#';  
                              has the same effect as the 'addfilename' option.  
          S.prefix  - prefix for the output file (default - 'c')  
         
          
        Dout        - MEEG object (also written to disk)  
       __________________________________________________________________________  
         
        This function can be used to merge M/EEG files to one file. This is  
        useful whenever the data are distributed over multiple files, but one  
        wants to use all information in one file. For example, when displaying  
        data (SPM displays data from only one file at a time), or merging  
        information that has been measured in multiple sessions.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_merge.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_merge", *args, **kwargs)
