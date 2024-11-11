from spm.__wrapper__ import Runtime


def _inifile(*args, **kwargs):
    """
     readsett = INIFILE(fileName,operation,keys,style)  
          Creates, reads, or writes data from/to ini (ascii) file.  
         
          - fileName:     ini file name  
          - operation:    can be one of the following:  
                          'new'       (rewrites an existing or creates a new, empty file),  
                          'deletekeys'(deletes keys and their values - if they exist),  
                          'read'      (reads values as strings),  
                          'write'     (writes values given as strings),  
          - keys:         cell-array of STRINGS; max 5 columns, min  
                          3 columns. Each row has the same number of columns. The columns are:  
                          'section':      section name string (the root is considered if empty or not given)  
                          'subsection':   subsection name string (the root is considered if empty or not given)  
                          'key':          name of the field to write/read from (given as a string).  
                          'value':        (optional) string-value to write to the ini file in case of 'write' operation  
                          'defaultValue': (optional) value that is returned when the key is not found when reading ('read' operation)  
          - style:        'tabbed' writes sections, subsections and keys in a tabbed style  
                          to get a more readable file. The 'plain' style is the  
                          default style. This only affects the keys that will be written/rewritten.  
         
          - readsett:     read setting in the case of the 'read' operation. If  
                          the keys are not found, the default values are returned  
                          as strings (if given in the 5-th column).  
         
          EXAMPLE:  
          Suppose we want a new ini file, test1.ini with 3 fields.  
          We can write them into the file using:  
         
          inifile('test1.ini','new');  
          writeKeys = {'measurement','person','name','Primoz Cermelj';...  
                       'measurement','protocol','id','1';...  
                       'application','','description','some...'};  
          inifile('test1.ini','write',writeKeys,'plain');  
         
          Later, you can read them out. Additionally, if any of them won't  
          exist, a default value will be returned (if the 5-th column is given as below).  
         
          readKeys = {'measurement','person','name','','John Doe';...  
                      'measurement','protocol','id','','0';...  
                      'application','','description','','none'};  
          readSett = inifile('test1.ini','read',readKeys);  
         
         
          NOTES: When the operation is 'new', only the first 2 parameters are  
          required. If the operation is 'write' and the file is empty or does not exist,  
          a new file is created. When writing and if any of the section or subsection or key does not exist,  
          it creates (adds) a new one.  
          Everything but value is NOT case sensitive. Given keys and values  
          will be trimmed (leading and trailing spaces will be removed).  
          Any duplicates (section, subsection, and keys) are ignored. Empty section and/or  
          subsection can be given as an empty string, '', but NOT as an empty matrix, [].  
         
          This function was tested on the win32 platform only but it should  
          also work on Unix/Linux platforms. Since some short-circuit operators  
          are used, at least Matlab 6.5 should be used.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/inifile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("inifile", *args, **kwargs)
