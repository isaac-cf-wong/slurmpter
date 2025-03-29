.. _tutorial:

:gitlab_url: https://gitlab.com/isaac-cfwong/slurmpter

********
Tutorial
********

-----------------------------------------
Build a simple workflow with only one job
-----------------------------------------

Suppose now you want to submit a single job to Slurm, the executable is ``<exec>`` with arguments ``<args>``.

.. code-block:: python

    from slurmpter import SlurmJob

    # Define the job directories to write submit files, standard outputs and standard errors.
    submit = "slurm/submit"
    output = "slurm/output"
    error = "slurm/error"

    # Construct a SlurmJob object to define the job.
    job = SlurmJob(name="job", executable="<exec>", submit=submit, output=output, error=error)
    job.add_arg("<args>")

    # Call build() to build the submit files but do not submit the jobs immediately.
    job.build()
    # Call build_submit() to build the submit files and submit the jobs sequentially.
    #job.build_submit()

If you want to run a Python script e.g. ``script.py``, replace ``<exec>`` with ``python`` and ``<args>`` with ``script.py``.

-----------------------------------------
Build a simple workflow with multiple jobs
-----------------------------------------

Suppose now you want to submit two jobs with different executables in a batch to Slurm,

.. code-block:: python

    from slurmpter import Slurm, SlurmJob

    # Define the job directories to write submit files, standard outputs and standard errors.
    submit = "slurm/submit"
    output = "slurm/output"
    error = "slurm/error"

    # Construct a Slurm object to hold all the jobs.
    slurm = Slurm(name="slurm", submit=submit)
    # Construct a SlurmJob object to define the first job.
    job_0 = SlurmJob(name="job_0", executable="<exec_0>", submit=submit, output=output, error=error, slurm=slurm)
    job_0.add_arg("<args_0>")

    # Construct another SlurmJob object to define the second job.
    job_1 = SlurmJob(name="job_1", executable="<exec_1>", submit=submit, output=output, error=error, slurm=slurm)
    job_1.add_arg("<args_1>")

    # Call build() to build the submit files but do not submit the jobs immediately.
    slurm.build()
    # Call build_submit() to build the submit files and submit the jobs sequentially.
    #slurm.build_submit()

Note that ``job_0`` and ``job_1`` do not have any inter-dependency, they can run concurrently if resource is available.

--------------------------------------------
Complex workflow with job inter-dependencies
--------------------------------------------

Please refer to :ref:`example <example>` for a more complex workflow.
