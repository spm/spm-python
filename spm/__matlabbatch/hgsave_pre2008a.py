from spm.__wrapper__ import Runtime


def hgsave_pre2008a(*args, **kwargs):
    """
      HGSAVE_PRE2008A  
        Starting with MATLAB 2008a, GUIDE saves figures with '%automatic'  
        functions (e.g. Callbacks, ResizeFcn ...) as anonymous function handles,  
        where previous versions used strings instead. The problem is that MATLAB  
        R14SP3 crashes on loading these anonymous function handles.  
         
        The problem can be resolved in 2 ways:   
        a) replacing anonymous function handles with string callbacks or  
        b) generating code with anonymous function handles which must be run in  
        MATLAB R14SP3 to save a valid .fig or .mat file.  
         
        function outfile = hgsave_pre2008a(figname,doreplace)  
        Input arguments:  
         figname   - string containing full path and file of .fig/.mat file to  
                     repair  
         doreplace - how to treat function handles  
                     true  - try to replace function handles with strings. Useful  
                             if one needs to be compatible, but has no R14SP3 at  
                             hand.  
                     false - create .m file that must be run in MATLAB R14SP3 to  
                             save a compatible .mat file.  
        Output argument:  
         outfile - file name of output file. Depending on doreplace, this is  
                   either a .fig/.mat file, or a .m file.  
          
        Details of the correction procedure:  
        1) load a MATLAB 2008a .fig or .mat file as variable  
        2) generate code for it using GENCODE  
        if doreplace  
          3) look for the characteristic regexp   
             @\(hObject,eventdata\)figname\(([^,]*).*  
          4) if found, replace it with string  
             figname($1,gcbo,[],guidata(gcbo))  
          if success  
            5) re-evaluate the code  
            6) save the new variable  
          else  
            generate semi-correct code  
          end  
        else  
          generate code without replacements  
        end  
         
        If there are other anonymous function handles left, the tool will create  
        an m-file with instructions which function handles may need to be  
        corrected. After editing, this m-file can be run to save the corrected  
        figure.  
         
        See also GENCODE, GENCODE_RVALUE, GENCODE_SUBSTRUCT, GENCODE_SUBSTRUCTCODE.  
         
        This code has been developed as part of a batch job configuration  
        system for MATLAB. See    
             http://sourceforge.net/projects/matlabbatch  
        for details about the original project.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/hgsave_pre2008a.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("hgsave_pre2008a", *args, **kwargs)
