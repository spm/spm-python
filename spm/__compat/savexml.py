from spm.__wrapper__ import Runtime


def savexml(*args, **kwargs):
    """
     SAVEXML Save workspace variables to disk in XML.  
         SAVEXML FILENAME saves all workspace variables to the XML-file  
         named FILENAME.xml. The data may be retrieved with LOADXML. if  
         FILENAME has no extension, .xml is assumed.  
           
         SAVE, by itself, creates the XML-file named 'matlab.xml'. It is  
         an error if 'matlab.xml' is not writable.  
         
         SAVE FILENAME X saves only X.  
         SAVE FILENAME X Y Z saves X, Y, and Z. The wildcard '*' can be   
         used to save only those variables that match a pattern.  
         
         SAVE ... -APPEND adds the variables to an existing file.  
         
         Use the functional form of SAVE, such as SAVE(filename','var1','var2'),  
         when the filename or variable names are stored in strings.  
         
         See also SAVE, MAT2XML, XMLTREE.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/savexml.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("savexml", *args, **kwargs, nargout=0)
