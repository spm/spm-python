from spm.__wrapper__ import Runtime


def spm_jobman(*args, **kwargs):
    """
      Main interface for SPM Batch System  
        This function provides a compatibility layer between SPM and matlabbatch.  
         
        FORMAT spm_jobman('initcfg')  
        Initialise jobs configuration and set MATLAB path accordingly.  
         
        FORMAT spm_jobman('run',job[,input1,...inputN])  
        FORMAT output_list = spm_jobman('run',job[,input1,...inputN])  
        FORMAT [output_list, hjob] = spm_jobman('run',job[,input1,...inputN])  
        Run specified job.  
        job         - filename of a job (.m or .mat), or  
                      cell array of filenames, or  
                      'jobs'/'matlabbatch' variable, or  
                      cell array of 'jobs'/'matlabbatch' variables.  
        input1,...  - optional list of input arguments. These are filled into  
                      open inputs ('X->' marked in the GUI) before a job is  
                      run. When using an "{:}" subscript on a cell array,  
                      MATLAB expands this cell array into a comma separated   
                      list of arguments. Therefore, one can collect input  
                      arguments in the right order into a cell array named e.g.  
                      input_array and call spm_jobman('run',job,input_array{:})  
                      to run a job using the collected inputs. For files or text  
                      entry items, these inputs are the values one would specify  
                      in the GUI. For menus, the item number has to be entered  
                      (neither the GUI label nor the associated value that is  
                      saved in a batch).  
        output_list - cell array containing the output arguments from each  
                      module in the job. The format and contents of these  
                      outputs is defined in the configuration of each module  
                      (.prog and .vout callbacks).  
        hjob        - harvested job after it has been filled and run. Note that  
                      this job has no dependencies any more. If one loads this  
                      job back to the batch system and changes some of the  
                      inputs, changed outputs will not be passed on.  
         
        FORMAT job_id = spm_jobman  
               job_id = spm_jobman('interactive',job[,node])  
               job_id = spm_jobman('interactive','',node)  
        Run the user interface in interactive mode.  
        job         - filename of a job (.m or .mat), or  
                      cell array of filenames, or  
                      'jobs'/'matlabbatch' variable, or  
                      cell array of 'jobs'/'matlabbatch' variables.  
        node        - indicate which part of the configuration is to be used.  
                      For example, it could be 'spm.spatial.coreg.estimate'.  
        job_id      - can be used to manipulate this job in cfg_util. Note that  
                      changes to the job in cfg_util will not show up in cfg_ui  
                      unless 'Update View' is called.  
         
        FORMAT jobs = spm_jobman('convert',jobs)  
        Convert older batch jobs to latest version  
        jobs        - char or cell array of filenames, or  
                      'jobs'/'matlabbbatch' variable  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_jobman.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_jobman", *args, **kwargs)
