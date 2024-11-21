from spm.__wrapper__ import Runtime


def matlab2markdown(*args, **kwargs):
    """
      MATLAB2MARKDOWN converts a MATLAB script or function to Markdown format. All  
        comments are converted to text, comment lines starting with %% are converted to  
        headings, sections with code are properly formatted, and words that appear in bold,  
        italic or monospace are converted.  
         
        Use as  
          matlab2markdown(infile, outfile, ...)  
         
        If no outfile is specified, it will write it to a .md file with the same name as  
        the infile. In case the file exists, it will be written with a numeric suffix.  
         
        The best is to provide the full filepath, otherwise it will look for the file within  
        the current path.  
         
        Optional input arguments can be specified as key-value pairs and can include  
          imagestyle = 'none|inline|jekyll'  
          pageheader = 'none|jekyll'  
          overwrite  = true/false, allow overwriting of the .md file (default = false)  
          highlight  = string, 'matlab', 'plaintext' or '' (default = '')  
          ...  
         
        See also MARKDOWN2MATLAB  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/matlab2markdown.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("matlab2markdown", *args, **kwargs, nargout=0)
