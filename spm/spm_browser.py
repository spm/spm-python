from spm.__wrapper__ import Runtime


def spm_browser(*args, **kwargs):
  """  Display an HTML document in a web browser  
    FORMAT spm_browser(url,[format])  
     
    url    - string containing URL (e.g. 'http://...' or 'file://...')  
    format - data format {['html'],'md'}  
             'md' option uses Markdown:  
               https://www.wikipedia.org/wiki/Markdown  
               http://showdownjs.com/  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_browser.m)
  """

  return Runtime.call("spm_browser", *args, **kwargs, nargout=0)
