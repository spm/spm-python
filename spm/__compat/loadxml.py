from spm.__wrapper__ import Runtime


def loadxml(*args, **kwargs):
    """
     LOADXML Load workspace variables from disk (XML file).  
         LOADXML FILENAME retrieves all variables from a file given a full   
         pathname or a MATLABPATH relative partial pathname (see PARTIALPATH).  
         If FILENAME has no extension LOAD looks for FILENAME and FILENAME.xml   
         and treats it as an XML file.   
           
         LOAD, by itself, uses the XML file named 'matlab.xml'. It is an error  
         if 'matlab.xml' is not found.  
         
         LOAD FILENAME X loads only X.  
         LOAD FILENAME X Y Z ... loads just the specified variables.  The  
         wildcard '*' loads variables that match a pattern.  
         Requested variables from FILENAME are created in the workspace.  
         
         S = LOAD(...) returns the contents of FILENAME in variable S. S is  
         a struct containing fields matching the variables retrieved.  
           
         Use the functional form of LOAD, such as LOAD('filename'), when the  
         file name is stored in a string, when an output argument is requested,  
         or if FILENAME contains spaces.  
         
         See also LOAD, XML2MAT, XMLTREE.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/loadxml.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("loadxml", *args, **kwargs)
