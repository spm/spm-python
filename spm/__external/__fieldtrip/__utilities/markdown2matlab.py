from spm.__wrapper__ import Runtime


def markdown2matlab(*args, **kwargs):
    """
      MARKDOWN2MATLAB converts a Markdown file to a MATLAB script or function. All text  
        is converted to comments, headings are converted to comment lines starting with %%  
        sections with code are properly formatted, and words that appear in bold, italic or  
        monospace are converted.  
         
        Use as  
          markdown2matlab(infile, outfile)  
         
        If no outfile is specified, it will write it to a .m file with the same name as  
        the infile. In case the file exists, it will be written with a numeric suffix.  
         
        The best is to provide the full filepath, otherwise it will look for the file within  
        the current path.  
         
        Optional input arguments can be specified as key-value pairs and can include  
          ...  
         
        See also MATLAB2MARKDOWN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/markdown2matlab.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("markdown2matlab", *args, **kwargs, nargout=0)
